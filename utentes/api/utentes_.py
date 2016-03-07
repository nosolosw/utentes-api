# -*- coding: utf-8 -*-

from pyramid.view import view_config
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from utentes.models.base import badrequest_exception
from utentes.models.utente import Utente



@view_config(route_name='utentes', request_method='GET', renderer='json')
@view_config(route_name='utentes_id', request_method='GET', renderer='json')
def utentes_get(request):
    gid = None
    if request.matchdict:
        gid = request.matchdict['id'] or None

    if gid: # return individual utente
        try:
            return request.db.query(Utente).filter(Utente.gid == gid).one()
        except(MultipleResultsFound, NoResultFound):
            raise badrequest_exception({
                'error': 'El código no existe',
                'gid': gid
                })
    else:
        return request.db.query(Utente).order_by(Utente.nome).all()

@view_config(route_name='utentes_id', request_method='DELETE', renderer='json')
def utentes_delete(request):
    gid = request.matchdict['id']
    if not gid:
        raise badrequest_exception({
            'error': 'gid es un campo necesario'
        })
    try:
        e = request.db.query(Utente).filter(Utente.gid == gid).one()
        request.db.delete(e)
        request.db.commit()
    except(MultipleResultsFound, NoResultFound):
        raise badrequest_exception({
            'error': 'El código no existe',
            'gid': gid
        })
    return {'gid': gid}

@view_config(route_name='utentes_id', request_method='PUT', renderer='json')
def utentes_update(request):
    gid = request.matchdict['id']
    if not gid:
        raise badrequest_exception({
            'error': 'gid es un campo necesario'
        })

    try:
        e = request.db.query(Utente).filter(Utente.gid == gid).one()
        e.update_from_json(request.json_body);
        request.db.add(e)
        request.db.commit()
    except(MultipleResultsFound, NoResultFound):
        raise badrequest_exception({
            'error': 'El código no existe',
            'gid': gid
        })
    except ValueError as ve:
        log.error(ve)
        raise badrequest_exception({'error':'body is not a valid json'})

    return e

@view_config(route_name='utentes', request_method='POST', renderer='json')
def utentes_create(request):
    try:
        body = request.json_body
        nome = body.get('nome')
    except ValueError as ve:
        log.error(ve)
        raise badrequest_exception({'error':'body is not a valid json'})

    if not nome:
        raise badrequest_exception({'error':'nome es un campo obligatorio'})

    e = request.db.query(Utente).filter(Utente.nome == nome).first()
    if e:
        raise badrequest_exception({'error':'La utente ya existe'})

    u = Utente.create_from_json(body)
    request.db.add(u)
    request.db.commit()
    return u
