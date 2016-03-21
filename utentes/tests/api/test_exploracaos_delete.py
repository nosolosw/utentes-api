# -*- coding: utf-8 -*-


import unittest
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from utentes.tests.api import DBIntegrationTest
from utentes.models.exploracao import Exploracao
from utentes.models.utente import Utente
from utentes.models.actividade import Actividade
from utentes.models.licencia import Licencia
from utentes.models.fonte import Fonte
from utentes.api.exploracaos import exploracaos_delete


class ExploracaosDeleteTests(DBIntegrationTest):

    def get_test_exploracao(self):
        EXP_ID = '2010-002'
        try:
            return self.request.db.query(Exploracao).filter(Exploracao.exp_id == EXP_ID).one()
        except (MultipleResultsFound, NoResultFound):
            return None

    def test_delete_get_exploracaos_id(self):
        exp = self.get_test_exploracao()
        gid = exp.gid
        gid_utente = exp.utente_rel.gid
        self.request.matchdict.update(dict(id=gid))
        exploracaos_delete(self.request)
        nro_exps = self.request.db.query(Exploracao).filter(Exploracao.gid == gid).count()
        nro_lics = self.request.db.query(Licencia).filter(Licencia.exploracao == gid).count()
        nro_fons = self.request.db.query(Licencia).filter(Fonte.exploracao == gid).count()
        nro_acts = self.request.db.query(Licencia).filter(Actividade.exploracao == gid).count()
        nro_utentes = self.request.db.query(Utente).filter(Utente.gid == gid_utente).count()
        self.assertEquals(0, nro_exps)
        self.assertEquals(0, nro_lics)
        self.assertEquals(0, nro_fons)
        self.assertEquals(0, nro_acts)
        self.assertEquals(1, nro_utentes)


if __name__ == '__main__':
    unittest.main()
