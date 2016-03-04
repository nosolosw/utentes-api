# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base

PGSQL_SCHEMA_UTENTES = 'utentes'
PGSQL_SCHEMA_DOMAINS = 'domains'

Base = declarative_base()


import json

def unauthorized_exception(body = None):
    body = body or {'error': 'No autorizado'}
    from pyramid.httpexceptions import HTTPUnauthorized
    return build_exception(HTTPUnauthorized, body)

def badrequest_exception(body = None):
    body = body or {'error': 'Peticion incorrecta'}
    from pyramid.httpexceptions import HTTPBadRequest
    return build_exception(HTTPBadRequest, body)

def notfound_exception(body = None):
    body = body or {'error': 'No encontrado'}
    from pyramid.httpexceptions import HTTPNotFound
    return build_exception(HTTPNotFound, body)

def methodnotallowed_exception(body = None):
    body = body or {'error': 'No permitido'}
    from pyramid.httpexceptions import HTTPMethodNotAllowed
    return build_exception(HTTPMethodNotAllowed, body)

def build_exception(httpexc, body):
    response = httpexc()
    response.body = json.dumps(body)
    response.content_type = 'application/json'
    return response


class APIAction(object):

    OK = 'ok'
    FAILED = 'failed'

    def __init__(self, operation="", status="", exp_type="", exp_id="",
                 user_name=""):
        self.operation = operation
        self.status = status
        self.exp_type = exp_type
        self.exp_id = exp_id
        self.user_name = user_name

    def __json__(self, request):
        return {
            'status':    self.status,
            'operation': self.operation,
            'type':      self.exp_type,
            'id':        self.exp_id,
            'name':      self.user_name
        }
