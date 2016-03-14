# -*- coding: utf-8 -*-


import unittest
from utentes.tests.api import DBIntegrationTest
from utentes.models.exploracao import Exploracao

# Asume que se está usando una base de datos con fixtures
# limpia
class ExploracaosPUT_IntegrationTests(DBIntegrationTest):


    def test_update_exploracao(self):
        from utentes.api.exploracaos import exploracaos_update
        self.request.matchdict.update( dict(id= 117) )
        exploracaos_update(self.request)
        actual = self.request.db.query(Exploracao).filter (Exploracao.gid == 117).count()
        expected = 0
        self.assertEquals(expected, actual)

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
        pass

    def test_update_exploracao_update_utente_validation_fails(self):
        pass

    def test_update_exploracao_rename_utente(self):
        pass

    def test_update_exploracao_rename_utente_validation_fails(self):
        pass



if __name__ == '__main__':
    unittest.main()
