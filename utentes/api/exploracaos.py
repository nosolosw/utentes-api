# -*- coding: utf-8 -*-

from pyramid.view import view_config

from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from utentes.models.utente import Utente
from utentes.models.exploracao import Exploracao
from utentes.models.base import badrequest_exception

@view_config(
    route_name='exploracao.json',
    request_method='GET',
    renderer='json')
def exploracao_get(request):
    exp_id = request.matchdict['exp_id']
    try:
        return request.db.query(Exploracao).filter(Exploracao.exp_id == exp_id).one()
    except(MultipleResultsFound, NoResultFound):
        raise badrequest_exception({
            'error': 'El código no existe',
            'exp_id': exp_id
        })

@view_config(
    route_name='exploracao.json',
    request_method='DELETE',
    renderer='json')
def exploracao_delete(request):
    exp_id = request.matchdict['exp_id']
    if not exp_id:
        raise badrequest_exception({
            'error': 'exp_id es un campo necesario'
        })
    try:
        e = request.db.query(Exploracao).filter(Exploracao.exp_id == exp_id).one()
        for f in e.fontes:
            # setting cascade in the relatioship is not working
            request.db.delete(f)
        for l in e.licencias:
            # setting cascade in the relatioship is not working
            request.db.delete(l)
        request.db.delete(e)
        request.db.commit()
    except(MultipleResultsFound, NoResultFound):
        raise badrequest_exception({
            'error': 'El código no existe',
            'exp_id': exp_id
        })
    return {'exp_id': exp_id}

@view_config(
    route_name='exploracaos.json',
    request_method='GET',
    renderer='json')
def exploracaos_get(request):
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
def exploracaos_geoms_get(request):
    exploracaos = []
    for e in request.db.query(Exploracao):
        exploracaos.append({
            'gid': e.gid,
            'the_geom': e.__json__(request)['the_geom']
        })
    return exploracaos

@view_config(
    route_name='exploracaos.json',
    request_method='POST',
    renderer='json')
def exploracaos_post(request):
    try:
        body = request.json_body
        exp_id = body.get('exp_id')
    except (ValueError):
        raise badrequest_exception({'error':'body is not a valid json'})

    if not exp_id:
        raise badrequest_exception({'error':'exp_id es un campo obligatorio'})

    e = request.db.query(Exploracao).filter(Exploracao.exp_id == exp_id).first()
    if e:
        raise badrequest_exception({'error':'La exploracao ya existe'})

    u = request.db.query(Utente).filter(Utente.nome == body.get('utente').get('nome')).first()
    if not u:
        u = Utente.create_from_json(body['utente'])
        request.db.add(u)
    e = Exploracao.create_from_json(body)
    e.utente_rel = u
    request.db.add(e)
    request.db.commit()
    return e
