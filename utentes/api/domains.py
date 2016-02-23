# -*- coding: utf-8 -*-

from pyramid.view import view_config
from utentes.models.utente import Utente
from utentes.models.domain import Domain

@view_config(
    route_name='domains.json',
    request_method='GET',
    renderer='json')
def domains_get(request):
    domains = request.db.query(Domain).all()
    for u in request.db.query(Utente):
        domains.append({
            'category': 'utente',
            'text': u.nome,
            'alias': '',
            'order': None,
            'parent': ''
        })
    return domains