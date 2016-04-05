# -*- coding: utf-8 -*-

from pyramid.view import view_config
from utentes.models.setting import Setting
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from utentes.models.base import badrequest_exception


@view_config(route_name='settings', request_method='GET', renderer='json')
def settings_get(request):
    return { s.property:s.value for s in request.db.query(Setting) }

@view_config(route_name='settings_property', request_method='PUT', renderer='json')
def settings_update(request):
    property = request.matchdict['property']
    if not property:
        raise badrequest_exception({'error': error_msgs['gid_obligatory']})

    try:
        setting = request.db.query(Setting).filter(Setting.property == property).one()
        setting.update_from_json(request.json_body, property)
        request.db.add(setting)
        request.db.commit()
    except(MultipleResultsFound, NoResultFound):
        raise badrequest_exception({
            'error': error_msgs['no_gid'],
            'gid': gid
        })
    except ValueError as ve:
        log.error(ve)
        raise badrequest_exception({'error': error_msgs['body_not_valid']})

    return setting
