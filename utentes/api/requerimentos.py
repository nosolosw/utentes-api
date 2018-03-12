# -*- coding: utf-8 -*-

from pyramid.view import view_config
from utentes.models.base import badrequest_exception
from utentes.models.exploracao import Exploracao
from utentes.api.error_msgs import error_msgs

import logging
log = logging.getLogger(__name__)


@view_config(route_name='api_requerimento_id', request_method='PATCH', renderer='json')
@view_config(route_name='api_requerimento_id', request_method='PUT', renderer='json')
def requerimento_update(request):
    gid = request.matchdict['id']
    body = request.json_body
    e = request.db.query(Exploracao).filter(Exploracao.gid == gid).one()
    import json
    e.observacio = json.dumps(body.get('observacio'))
    e.exp_name = body.get('exp_name', e.exp_name)
    request.db.add(e)
    request.db.commit()
    return e


@view_config(route_name='api_requerimento', request_method='POST', renderer='json')
# admin || administrativo
def requerimento_create(request):
    try:
        body = request.json_body
    except ValueError as ve:
        log.error(ve)
        raise badrequest_exception({'error': error_msgs['body_not_valid']})

    e = Exploracao()
    e.exp_id = calculate_new_exp_id()

    # Introducido a boleo por el administrativo
    # Será cambiado a posteriori
    e.exp_name = body.get('exp_name')

    import json
    e.observacio = json.dumps(body.get('observacio'))

    # exp_id, exp_name, loc_provin, loc_distri, loc_posto, utente son not null
    # * rellenar a un genérico "Desconhecido"
    # * Poner como nullables
    # * Nueva tabla requirimentos y no usar explotaciones
    # Si se usa la tabla de explotaciones seguramente hace falta un campo 'active' y filrar por él

    # Problemas con las validaciones
    # Exploracao.create_from_json(body)

    e.loc_provin = 'Cabo Delgado'
    e.loc_distri = 'Palma'
    e.loc_posto = 'Palma'
    e.utente = 55

    request.db.add(e)
    request.db.commit()
    return e


def calculate_new_exp_id():
    import random
    return str(random.randint(1, 100000))
