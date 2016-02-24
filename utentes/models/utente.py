# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text, text

from .base import Base, PGSQL_SCHEMA_UTENTES

class Utente(Base):
    __tablename__ = 'utentes'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('utentes.utentes_gid_seq'::regclass)"))
    nome = Column(Text, nullable=False, unique=True)
    nuit = Column(Text, unique=True)
    entidade = Column(Text)
    reg_comerc = Column(Text)
    reg_zona = Column(Text)

    @staticmethod
    def create_from_json(json):
        u = Utente()
        u.nome = json.get('nome')
        u.nuit = json.get('nuit')
        u.entidade = json.get('entidade')
        u.reg_comerc = json.get('reg_comerc')
        return u

    def __json__(self, request):
        return {
            'id': self.gid,
            'nome': self.nome,
            'nuit': self.nuit,
            'entidade': self.entidade,
            'reg_comerc': self.reg_comerc,
            'reg_zona': self.reg_zona
            }
