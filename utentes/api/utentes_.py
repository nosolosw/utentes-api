# -*- coding: utf-8 -*-

from pyramid.view import view_config
from utentes.models.utente import Utente

@view_config(
    route_name='utentes.json',
    request_method='GET',
    renderer='json')
def utentes_get(request):
    return request.db.query(Utente).all()
