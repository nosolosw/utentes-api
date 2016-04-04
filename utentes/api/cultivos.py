# -*- coding: utf-8 -*-

from pyramid.view import view_config
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from utentes.lib.schema_validator.validator import Validator
from utentes.models.base import badrequest_exception
from utentes.models.actividades_schema import ActividadeSchema
from utentes.models.cultivo import ActividadesCultivos


@view_config(route_name='cultivos', request_method='GET', renderer='json')
@view_config(route_name='cultivos_id', request_method='GET', renderer='json')
def cultivos_get(request):
    gid = None
    if request.matchdict:
        gid = request.matchdict['id'] or None

    if gid:  # return individual cultivo
        try:
            return request.db.query(ActividadesCultivos).filter(ActividadesCultivos.gid == gid).one()
        except(MultipleResultsFound, NoResultFound):
            raise badrequest_exception({
                'error': error_msgs['no_gid'],
                'gid': gid
                })
    else:  # return collection
        return {
            'type': 'FeatureCollection',
            'features': request.db.query(ActividadesCultivos).order_by(ActividadesCultivos.cult_id).all()
        }



@view_config(route_name='cultivos_id', request_method='PUT', renderer='json')
def cultivos_update(request):
    gid = request.matchdict['id']
    if not gid:
        raise badrequest_exception({'error': error_msgs['gid_obligatory']})

    msgs = validate_entities(request.json_body)
    if len(msgs) > 0:
        raise badrequest_exception({'error': msgs})

    try:
        e = request.db.query(Utente).filter(Utente.gid == gid).one()
        e.update_from_json(request.json_body)
        request.db.add(e)
        request.db.commit()
    except(MultipleResultsFound, NoResultFound):
        raise badrequest_exception({
            'error': error_msgs['no_gid'],
            'gid': gid
        })
    except ValueError as ve:
        log.error(ve)
        raise badrequest_exception({'error': error_msgs['body_not_valid']})

    return e



def validate_entities(body):
    return Validator(UTENTE_SCHEMA).validate(body)
