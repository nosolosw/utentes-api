# -*- coding: utf-8 -*-


import unittest
from utentes.tests.api import DBIntegrationTest

# Asume que se está usando una base de datos con fixtures
# limpia
class ExploracaosGET_IntegrationTests(DBIntegrationTest):

    def test_lengh_of_get_exploracaos(self):
        from utentes.api.exploracaos import exploracaos_get
        actual = exploracaos_get(self.request)
        expected_len = 46
        self.assertEquals(len(actual['features']), expected_len)

    def test_properties_exists_in_get_exploracaos_id(self):
        from utentes.api.exploracaos import exploracaos_get
        self.request.matchdict.update( dict(id= 117) )
        actual = exploracaos_get(self.request).__json__(self.request)
        self.assertTrue('geometry' in actual)
        self.assertTrue('type' in actual)
        self.assertTrue('properties' in actual)

if __name__ == '__main__':
    unittest.main()
