# -*- coding: utf-8 -*-


import unittest
from utentes.tests.api import DBIntegrationTest
from utentes.models.exploracao import Exploracao

# Asume que se está usando una base de datos con fixtures
# limpia
class ExploracaosDELETE_IntegrationTests(DBIntegrationTest):


    def test_delete_get_exploracaos_id(self):
        from utentes.api.exploracaos import exploracaos_delete
        self.request.matchdict.update( dict(id= 117) )
        exploracaos_delete(self.request)
        actual = self.request.db.query(Exploracao).filter (Exploracao.gid == 117).count()
        expected = 0
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
