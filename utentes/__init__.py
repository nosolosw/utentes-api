# -*- coding: utf-8 -*-

from pyramid.config import Configurator
from pyramid.request import Request
from pyramid.decorator import reify
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker


class RequestWithDB(Request):

    @reify
    def db(self):
        """Return a session. Only called once per request,
        thanks to @reify decorator"""
        session_factory = self.registry.settings['db.session_factory']
        self.add_finished_callback(self.close_db_connection)
        return session_factory()

    def close_db_connection(self, request):
        request.db.commit()
        request.db.close()


def date_adapter(obj, request):
    return obj.strftime('%d/%m/%Y') if obj else ''

def decimal_adapter(obj, request):
    return str(obj) if obj or obj == 0 else ''

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    session_factory = sessionmaker(bind=engine)
    settings['db.session_factory'] = session_factory

    config = Configurator(
        settings=settings,
        request_factory = RequestWithDB
    )

    from pyramid.renderers import JSON
    json_renderer = JSON()
    import datetime
    json_renderer.add_adapter(datetime.date, date_adapter)
    from decimal import Decimal
    json_renderer.add_adapter(Decimal, decimal_adapter)
    config.add_renderer('json', json_renderer)

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('exploracao.json', '/exploracao/{exp_id}.json')

    config.scan()
    return config.make_wsgi_app()


