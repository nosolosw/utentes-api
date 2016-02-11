# -*- coding: utf-8 -*-

from pyramid.view import view_config

from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from utentes.models.models import Exploracao, Fonte, Licencia, Utente
from utentes.models.base import badrequest_exception

@view_config(
    route_name='exploracao.json',
    request_method='GET',
    renderer='json')
def exploracao(request):
    exp_id = request.matchdict['exp_id']
    try:
        return request.db.query(Exploracao).filter(Exploracao.exp_id == exp_id).one()
    except(MultipleResultsFound, NoResultFound):
        raise badrequest_exception({
            'error': 'El código no existe',
            'exp_id': exp_id
        })

@view_config(
    route_name='exploracaos.json',
    request_method='GET',
    renderer='json')
def exploracaos(request):
    exploracaos = []
    for e in request.db.query(Exploracao):
        exploracaos.append({
            'gid': e.gid,
            'exp_name': e.exp_name,
            'exp_id': e.exp_id,
            'licencia': ' ?? ',
            'consumo': ' ?? ',
            'pagos': e.pagos,
            'utente': e.utente_rel.nome
        })
    return exploracaos

@view_config(
    route_name='exploracaos.geojson',
    request_method='GET',
    renderer='json')
def exploracaos_geoms(request):
    exploracaos = []
    for e in request.db.query(Exploracao):
        exploracaos.append({
            'gid': e.gid,
            'the_geom': e.__json__(request)['the_geom']
        })
    return exploracaos
