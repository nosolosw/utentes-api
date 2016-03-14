# -*- coding: utf-8 -*-


import unittest
from utentes.tests.api import DBIntegrationTest
from utentes.models.exploracao import Exploracao

# Asume que se está usando una base de datos con fixtures
# limpia
class ExploracaosPOST_IntegrationTests(DBIntegrationTest):


    def test_create_exploracao(self):
        pass

    def test_create_exploracao_validation_fails(self):
        pass


    def test_create_exploracao_create_fonte(self):
        pass

    def test_create_exploracao_create_fonte_validation_fails(self):
        pass



    def test_create_exploracao_create_licencia(self):
        pass

    def test_create_exploracao_create_licencia_validation_fails(self):
        pass




    def test_create_exploracao_create_actividade(self):
        pass

    def test_create_exploracao_create_actividade_validation_fails(self):
        pass



    def test_create_exploracao_create_utente(self):
        pass

    def test_create_exploracao_create_utente_validation_fails(self):
        pass





if __name__ == '__main__':
    unittest.main()
