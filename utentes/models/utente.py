# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text, text
from sqlalchemy.orm import relationship
from .base import Base, PGSQL_SCHEMA_UTENTES

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
        u.nome       = json.get('nome')
        u.nuit       = json.get('nuit')
        u.entidade   = json.get('entidade')
        u.reg_comerc = json.get('reg_comerc')
        u.loc_provin = json.get('loc_provin')
        u.loc_distri = json.get('loc_distri')
        u.loc_posto  = json.get('loc_posto')
        u.loc_nucleo = json.get('loc_nucleo')
        u.observacio = json.get('observacio')
        return u

    def __json__(self, request):
        return {
            'id':         self.gid,
            'nome':       self.nome,
            'nuit':       self.nuit,
            'entidade':   self.entidade,
            'reg_comerc': self.reg_comerc,
            'reg_zona':   self.reg_zona,
            'loc_provin': self.loc_provin,
            'loc_distri': self.loc_distri,
            'loc_posto':  self.loc_posto,
            'loc_nucleo': self.loc_nucleo,
            'observacio': self.observacio,
            }
