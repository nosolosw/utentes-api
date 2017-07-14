# -*- coding: utf-8 -*-

import unittest

from pyramid import testing
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

settings = get_appsettings('development.ini', 'main')
engine = engine_from_config(settings, 'sqlalchemy.')
session_factory = sessionmaker()


class DBIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        self.connection = engine.connect()
        self.transaction = self.connection.begin()
        self.db_session = session_factory(bind=self.connection)
        self.request = testing.DummyRequest()
        self.request.db = self.db_session

    def tearDown(self):
        testing.tearDown()
        self.transaction.rollback()
        self.db_session.close()
        self.connection.close()
