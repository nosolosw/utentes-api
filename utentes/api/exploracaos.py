# -*- coding: utf-8 -*-

from pyramid.view import view_config

from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from utentes.models.utente import Utente
from utentes.models.utente_schema import UTENTE_SCHEMA
from utentes.models.exploracao import Exploracao
from utentes.models.exploracao_schema import EXPLORACAO_SCHEMA
from utentes.models.base import badrequest_exception
from utentes.lib.validator import Validator


@view_config(route_name='exploracaos',    request_method='GET', renderer='json')
@view_config(route_name='exploracaos_id', request_method='GET', renderer='json')
def exploracaos_get(request):
    gid = None
    if request.matchdict:
        gid = request.matchdict['id'] or None

    if gid: # return individual explotacao
        try:
            return request.db.query(Exploracao).filter(Exploracao.gid == gid).one()
        except(MultipleResultsFound, NoResultFound):
            raise badrequest_exception({
                'error': 'El código no existe',
                'gid': gid
                })

    else: # return collection
        return {
            'type': 'FeatureCollection',
            'features': request.db.query(Exploracao).all()
        }


@view_config(route_name='exploracaos_id', request_method='DELETE', renderer='json')
def exploracaos_delete(request):
    gid = request.matchdict['id']
    if not gid:
        raise badrequest_exception({
            'error': 'gid es un campo necesario'
        })
    try:
        e = request.db.query(Exploracao).filter(Exploracao.gid == gid).one()
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
            'gid': gid
        })
    return {'gid': gid}

@view_config(route_name='exploracaos', request_method='POST', renderer='json')
def exploracaos_create(request):
    try:
        body = request.json_body
        exp_id = body.get('exp_id')
    except (ValueError):
        raise badrequest_exception({'error':'body is not a valid json'})

    validatorExploracao = Validator(EXPLORACAO_SCHEMA)
    msgs = validatorExploracao.validate(body)
    validatorUtente = Validator(UTENTE_SCHEMA)
    msgs = msgs + validatorUtente.validate(body['utente'])
    if len(msgs) > 0:
        raise badrequest_exception({'error': msgs})

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
