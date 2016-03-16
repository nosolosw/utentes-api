# -*- coding: utf-8 -*-


import unittest
from utentes.tests.api import DBIntegrationTest
from utentes.models.exploracao import Exploracao
from utentes.models.utente import Utente
from utentes.api.exploracaos import exploracaos_update

# Asume que se está usando una base de datos con fixtures limpia
MAGIC_GID = 117

class ExploracaosPUT_IntegrationTests(DBIntegrationTest):


    def test_update_exploracao(self):
        pass

    def test_update_exploracao_validation_fails(self):
        pass



    def test_update_exploracao_update_fonte(self):
        pass

    def test_update_exploracao_update_fonte_validation_fails(self):
        pass

    def test_update_exploracao_create_fonte(self):
        pass

    def test_update_exploracao_create_fonte_validation_fails(self):
        pass

    def test_update_exploracao_delete_fonte(self):
        pass



    def test_update_exploracao_update_licencia(self):
        pass

    def test_update_exploracao_update_licencia_validation_fails(self):
        pass

    def test_update_exploracao_create_licencia(self):
        pass

    def test_update_exploracao_create_licencia_validation_fails(self):
        pass

    def test_update_exploracao_delete_licencia(self):
        pass





    def test_update_exploracao_update_actividade(self):
        self.request.matchdict.update( dict(id= MAGIC_GID) )
        expected = self.request.db.query(Exploracao).filter(Exploracao.gid == MAGIC_GID).first()
        expected_json = self._build_json(expected)
        expected_json['actividade']['c_estimado'] = 101.11
        self.request.json_body = expected_json
        exploracaos_update(self.request)
        actual = self.request.db.query(Exploracao).filter(Exploracao.gid == MAGIC_GID).first()
        self.assertEquals(101.11, float(actual.actividade.c_estimado))

    def test_update_exploracao_update_actividade_validation_fails(self):
        self.request.matchdict.update( dict(id= MAGIC_GID) )
        expected = self.request.db.query(Exploracao).filter(Exploracao.gid == MAGIC_GID).first()
        expected_json = self._build_json(expected)
        expected_json['utente']['observacio'] = ' foo - bar '
        expected_json['observacio'] = ' foo - bar '
        expected_json['actividade']['c_estimado'] = 'TEXT'
        self.request.json_body = expected_json
        from pyramid.httpexceptions import HTTPBadRequest
        self.assertRaises(HTTPBadRequest, exploracaos_update, self.request)

        s = self._create_new_session()
        actual = s.query(Exploracao).filter(Exploracao.gid == MAGIC_GID).first()
        self.assertEquals(expected.utente_rel.observacio, actual.utente_rel.observacio)
        self.assertNotEquals(' foo - bar ', actual.utente_rel.observacio)
        self.assertEquals(expected.observacio, actual.observacio)
        self.assertNotEquals(' foo - bar ', actual.observacio)


    def test_update_exploracao_create_actividade(self):
        pass

    def test_update_exploracao_create_actividade_validation_fails(self):
        pass

    def test_update_exploracao_delete_actividade(self):
        pass

    def test_update_exploracao_update_actividade_tipo(self):
        pass

    def test_update_exploracao_update_utente(self):
        self.request.matchdict.update( dict(id= MAGIC_GID) )
        expected = self.request.db.query(Exploracao).filter(Exploracao.gid == MAGIC_GID).first()
        expected_json = self._build_json(expected)
        expected_json['utente']['observacio'] = 'foo - bar'
        self.request.json_body = expected_json
        exploracaos_update(self.request)
        actual = self.request.db.query(Exploracao).filter(Exploracao.gid == MAGIC_GID).first()
        self.assertEquals('foo - bar', actual.utente_rel.observacio)

    def test_update_exploracao_update_utente_validation_fails(self):
        self.request.matchdict.update( dict(id= MAGIC_GID) )
        expected = self.request.db.query(Exploracao).filter(Exploracao.gid == MAGIC_GID).first()
        expected_json = self._build_json(expected)
        expected_json['utente']['nome'] = None
        self.request.json_body = expected_json
        from pyramid.httpexceptions import HTTPBadRequest
        self.assertRaises(HTTPBadRequest, exploracaos_update, self.request)

        s = self._create_new_session()
        actual = s.query(Exploracao).filter(Exploracao.gid == MAGIC_GID).first()
        self.assertEquals(expected.utente_rel.nome, actual.utente_rel.nome)


    def test_update_exploracao_rename_utente(self):
        '''
        Tests that the related utente can be renamed from the exploracao,
        and a new utente is not created
        '''
        self.request.matchdict.update( dict(id= MAGIC_GID) )
        expected = self.request.db.query(Exploracao).filter(Exploracao.gid == MAGIC_GID).first()
        expected_utente_gid = expected.utente
        expected_json = self._build_json(expected)
        expected_json['utente']['nome'] = 'foo - bar'
        self.request.json_body = expected_json
        exploracaos_update(self.request)
        actual = self.request.db.query(Exploracao).filter(Exploracao.gid == MAGIC_GID).first()
        self.assertEquals(expected_utente_gid, actual.utente)
        self.assertEquals('foo - bar', actual.utente_rel.nome)
        u = self.request.db.query(Utente).filter(Utente.gid == expected_utente_gid).first()
        self.assertEquals('foo - bar', u.nome)

    def test_update_exploracao_rename_utente_validation_fails(self):
        self.request.matchdict.update( dict(id= MAGIC_GID) )
        expected = self.request.db.query(Exploracao).filter(Exploracao.gid == MAGIC_GID).first()
        expected_utente_gid = expected.utente
        expected_json = self._build_json(expected)
        expected_json['utente']['nome'] = 'foo - bar'
        expected_json['c_soli'] = 'text'
        self.request.json_body = expected_json
        from pyramid.httpexceptions import HTTPBadRequest
        self.assertRaises(HTTPBadRequest, exploracaos_update, self.request)

    def _build_json(self, e):
        expected_json = e.__json__(self.request)
        expected_json.update ( expected_json.pop('properties') )
        expected_json['fontes'] = [f.__json__(self.request) for f in expected_json['fontes']]
        expected_json['licencias'] = [f.__json__(self.request) for f in expected_json['licencias']]
        expected_json['actividade'] = expected_json['actividade'].__json__(self.request)
        return expected_json

    def _create_new_session(self):
        # La idea de generar una sesión distinta para este último chequeo
        # es que no haya cosas cacheadas en la sesión original
        from pyramid.paster import get_appsettings
        from sqlalchemy import engine_from_config
        from sqlalchemy.orm import sessionmaker
        settings = get_appsettings('development.ini', 'main')
        engine = engine_from_config(settings, 'sqlalchemy.')
        session = sessionmaker()
        session.configure(bind=engine)
        return session()

if __name__ == '__main__':
    unittest.main()
