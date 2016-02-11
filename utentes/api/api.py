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
