# -*- coding: utf-8 -*-

from pyramid.view import view_config
from utentes.models.inventario_fonte import InventarioFonte
from error_msgs import error_msgs
from utentes.models.base import badrequest_exception
import json

import logging
log = logging.getLogger(__name__)


@view_config(route_name='api_base_fountains', request_method='POST', renderer='json')
def base_fountains_post(request):
    body = request.json_body
    # try:
    #     request.db.query(InventarioFonte).delete()
    #     f = InventarioFonte.create_from_json(body['features'][0])
    #     for feat in body['features']:
    #         f = InventarioFonte.create_from_json(feat)
    #         request.db.add(f)
    #     request.db.commit()
    #     return {'msg': 'Carregadas %d fontes' % len(body['features'])}
    # except Exception as e:
    #     log.error(e)
    #     request.db.rollback()
    #     raise badrequest_exception({'error': error_msgs['bad_import_file']})
    try:
        import os
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        path = os.path.join(dir_path, 'static', 'utentes-ui', 'offline', 'data', 'json_Fontes.js')
        with open(path, "w") as f:
            f.write(json.dumps(body))
        return {'msg': 'Carregadas %d fontes' % len(body['features'])}
    except Exception as e:
        log.error(e)
        raise badrequest_exception({'error': error_msgs['bad_import_file']})


@view_config(route_name='api_base_fountains', request_method='GET', renderer='json')
def base_fountains_get(request):
    return {
        'type': 'FeatureCollection',
        'features': request.db.query(InventarioFonte).all()
    }
