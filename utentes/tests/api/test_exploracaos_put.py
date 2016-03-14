# -*- coding: utf-8 -*-


import unittest
from utentes.tests.api import DBIntegrationTest
from utentes.models.exploracao import Exploracao
from utentes.models.utente import Utente

# Asume que se está usando una base de datos con fixtures
# limpia
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
        pass

    def test_update_exploracao_update_actividade_validation_fails(self):
        pass

    def test_update_exploracao_create_actividade(self):
        pass

    def test_update_exploracao_create_actividade_validation_fails(self):
        pass

    def test_update_exploracao_delete_actividade(self):
        pass



    def test_update_exploracao_update_utente(self):
        from utentes.api.exploracaos import exploracaos_update
        self.request.matchdict.update( dict(id= 117) )
        expected = self.request.db.query(Exploracao).filter(Exploracao.gid == 117).first()
        expected_json = expected.__json__(self.request)
        expected_json.update ( expected_json.pop('properties') )
        expected_json['fontes'] = [f.__json__(self.request) for f in expected_json['fontes']]
        expected_json['licencias'] = [f.__json__(self.request) for f in expected_json['licencias']]
        expected_json['utente'] = expected_json['utente'].__json__(self.request)
        expected_json['utente']['observacio'] = 'foo - bar'
        self.request.json_body = expected_json
        exploracaos_update(self.request)
        actual = self.request.db.query(Exploracao).filter(Exploracao.gid == 117).first()
        self.assertEquals('foo - bar', actual.utente_rel.observacio)

    def test_update_exploracao_update_utente_validation_fails(self):
        from utentes.api.exploracaos import exploracaos_update
        self.request.matchdict.update( dict(id= 117) )
        expected = self.request.db.query(Exploracao).filter(Exploracao.gid == 117).first()
        expected_json = expected.__json__(self.request)
        expected_json.update ( expected_json.pop('properties') )
        expected_json['fontes'] = [f.__json__(self.request) for f in expected_json['fontes']]
        expected_json['licencias'] = [f.__json__(self.request) for f in expected_json['licencias']]
        expected_json['utente'] = expected_json['utente'].__json__(self.request)
        expected_json['utente']['nome'] = None
        self.request.json_body = expected_json
        from pyramid.httpexceptions import HTTPBadRequest
        self.assertRaises(HTTPBadRequest, exploracaos_update, self.request)

        # La idea de generar una sesión distinta para este último chequeo
        # es que no haya cosas cacheadas en la sesión original
        from pyramid.paster import get_appsettings
        from sqlalchemy import engine_from_config
        from sqlalchemy.orm import sessionmaker
        settings = get_appsettings('development.ini', 'main')
        engine = engine_from_config(settings, 'sqlalchemy.')
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        actual = s.query(Exploracao).filter(Exploracao.gid == 117).first()
        self.assertEquals(expected.utente_rel.nome, actual.utente_rel.nome)


    def test_update_exploracao_rename_utente(self):
        '''
        Tests that the related utente can be renamed from the exploracao,
        and a new utente is not created
        '''
        from utentes.api.exploracaos import exploracaos_update
        self.request.matchdict.update( dict(id= 117) )
        expected = self.request.db.query(Exploracao).filter(Exploracao.gid == 117).first()
        expected_utente_gid = expected.utente
        expected_json = expected.__json__(self.request)
        expected_json.update ( expected_json.pop('properties') )
        expected_json['fontes'] = [f.__json__(self.request) for f in expected_json['fontes']]
        expected_json['licencias'] = [f.__json__(self.request) for f in expected_json['licencias']]
        expected_json['utente'] = expected_json['utente'].__json__(self.request)
        expected_json['utente']['nome'] = 'foo - bar'
        self.request.json_body = expected_json
        exploracaos_update(self.request)
        actual = self.request.db.query(Exploracao).filter(Exploracao.gid == 117).first()
        self.assertEquals(expected_utente_gid, actual.utente)
        self.assertEquals('foo - bar', actual.utente_rel.nome)
        u = self.request.db.query(Utente).filter(Utente.gid == expected_utente_gid).first()
        self.assertEquals('foo - bar', u.nome)

    def test_update_exploracao_rename_utente_validation_fails(self):
        from utentes.api.exploracaos import exploracaos_update
        self.request.matchdict.update( dict(id= 117) )
        expected = self.request.db.query(Exploracao).filter(Exploracao.gid == 117).first()
        expected_utente_gid = expected.utente
        expected_json = expected.__json__(self.request)
        expected_json.update ( expected_json.pop('properties') )
        expected_json['fontes'] = [f.__json__(self.request) for f in expected_json['fontes']]
        expected_json['licencias'] = [f.__json__(self.request) for f in expected_json['licencias']]
        expected_json['utente'] = expected_json['utente'].__json__(self.request)
        expected_json['utente']['nome'] = 'foo - bar'
        expected_json['c_soli'] = 'text'
        self.request.json_body = expected_json
        from pyramid.httpexceptions import HTTPBadRequest
        self.assertRaises(HTTPBadRequest, exploracaos_update, self.request)




if __name__ == '__main__':
    unittest.main()
