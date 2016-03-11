# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text, text
from sqlalchemy.orm import relationship

from utentes.models.base import Base, PGSQL_SCHEMA_UTENTES


class Utente(Base):
    __tablename__ = 'utentes'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid        = Column(Integer, primary_key=True, server_default=text("nextval('utentes.utentes_gid_seq'::regclass)"))
    nome       = Column(Text, nullable=False, unique=True)
    nuit       = Column(Text, unique=True)
    entidade   = Column(Text)
    reg_comerc = Column(Text)
    reg_zona   = Column(Text)
    loc_provin = Column(Text)
    loc_distri = Column(Text)
    loc_posto  = Column(Text)
    loc_nucleo = Column(Text)
    observacio = Column(Text)

    exploracaos = relationship('Exploracao',
                               backref='utente_rel',
                               passive_deletes=True)

    @staticmethod
    def create_from_json(json):
        u = Utente()
        u.update_from_json(json)
        return u

    def update_from_json(self, json):
        self.gid        = json.get('id') or None
        self.nome       = json.get('nome')
        self.nuit       = json.get('nuit')
        self.entidade   = json.get('entidade')
        self.reg_comerc = json.get('reg_comerc')
        self.reg_zona   = json.get('reg_zona')
        self.loc_provin = json.get('loc_provin')
        self.loc_distri = json.get('loc_distri')
        self.loc_posto  = json.get('loc_posto')
        self.loc_nucleo = json.get('loc_nucleo')
        self.observacio = json.get('observacio')

    # python uses this method to compare objects
    # for example, in exploracao.update_array
    def __eq__(self, other):
        if (self.gid is None) or (other.gid is None):
            # shall we in this case compare all attributes?
            return False
        return self.gid == other.gid

    def __json__(self, request):
        exploracaos = []
        for e in self.exploracaos:
            exploracaos.append({
                'gid':        e.gid,
                'exp_name':   e.exp_name,
                'exp_id':     e.exp_id,
                'actividade': e.actividade
            })

        return {
            'id':          self.gid,
            'nome':        self.nome,
            'nuit':        self.nuit,
            'entidade':    self.entidade,
            'reg_comerc':  self.reg_comerc,
            'reg_zona':    self.reg_zona,
            'loc_provin':  self.loc_provin,
            'loc_distri':  self.loc_distri,
            'loc_posto':   self.loc_posto,
            'loc_nucleo':  self.loc_nucleo,
            'observacio':  self.observacio,
            'exploracaos': exploracaos
            }
