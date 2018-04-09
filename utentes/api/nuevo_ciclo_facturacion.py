# -*- coding: utf-8 -*-

from pyramid.view import view_config
from utentes.models.exploracao import Exploracao

import logging
log = logging.getLogger(__name__)


@view_config(route_name='nuevo_ciclo_facturacion', request_method='POST', renderer='json')
# admin || financieiro
def nuevo_ciclo_facturacion(request):
    import json
    exps = request.db.query(Exploracao).all()
    for e in exps:
        for l in e.licencias:
            if l.estado == 'Licenciada':
                try:
                    observacio = json.loads(e.observacio)
                except (TypeError, ValueError):
                    observacio = {
                        'analisis_doc': False,
                        'sol_visita': False,
                        'parecer_unidade': False,
                        'parecer_tecnico': False,

                        'juri2_doc_legal': False,
                        'juri2_parecer_tecnico': False,
                        'juri2_parecer_relevantes': False,
                        'comments': [],

                        'consumo_tipo': 'Variável',

                        'pago_lic': 'Não',
                        'pago_c_mes': 'Não',
                        'factura_emitida': 'Não',


                        'estado_facturacion': 'pendiente_consumo',
                        'facturacion': []
                    }
                observacio['facturacion'] = observacio['facturacion'] or []

                estado_facturacion = u'Variável'
                if observacio.get('consumo_tipo') == u'Variável':
                    estado_facturacion = 'pendiente_consumo'
                elif observacio.get('consumo_tipo') == u'Fixo':
                    estado_facturacion = 'pendiente_factura'

                # Tal vez meter fecha
                pago_lic = 'Não'
                if len(observacio['facturacion']) > 0:
                    pago_lic = observacio['facturacion'][-1]['pago_lic']

                import datetime
                currentFact = {
                    'estado_facturacion': estado_facturacion,
                    'date_reset': datetime.datetime.now().isoformat(),

                    'c_facturado': decimal_adapter(e.c_licencia),
                    'taxa_fixa': decimal_adapter(l.taxa_fixa),
                    'taxa_uso': decimal_adapter(l.taxa_uso),
                    'pago_mes': decimal_adapter(l.pago_mes),
                    'pago_c_mes': 'Não',
                    'pago_lic': pago_lic,
                    'factura_emitida': 'Não',
                    'iva': decimal_adapter(l.iva),
                    'pago_iva': decimal_adapter(l.pago_iva),
                    'comments': [],
                }
                observacio['facturacion'].append(currentFact)
                observacio['estado_facturacion'] = estado_facturacion
                e.observacio = json.dumps(observacio)
                # e.estado_facturacion = 'pendiente_consumo'
                request.db.add(e)

    request.db.commit()
    return {'ok': 'ok'}


def decimal_adapter(obj):
    return float(obj) if obj or (obj == 0) else None
