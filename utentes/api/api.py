# -*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from utentes.models.models import MyModel
from utentes.models.base import badrequest_exception

@view_config(
    route_name='home',
    request_method='GET',
    renderer='json')
def my_view(request):
    try:
        return request.db.query(MyModel).filter(MyModel.auth_srid == 32727).one()
    except(MultipleResultsFound, NoResultFound):
        raise badrequest_exception({
            'error': 'El código no existe',
            'srid': 32727
        })
