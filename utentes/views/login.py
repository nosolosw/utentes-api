# -*- coding: utf-8 -*-
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

VALID_LOGINS = ['admin', 'administrativo', 'financieiro', 'secretaria', 'tecnico', 'juridico']


@view_config(route_name='login', renderer='utentes:templates/login.jinja2')
def login(request):

    if 'submit' in request.POST:
        login_user = request.POST.get('user', '')

        if login_user in VALID_LOGINS:
            response = HTTPFound(
                location='/static/utentes-ui/pendentes.html',
            )
            response.set_cookie('utentes_stub_user', value=login_user)
            return response
    return {'title': 'Login Utentes'}
