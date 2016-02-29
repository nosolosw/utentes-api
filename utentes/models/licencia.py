# -*- coding: utf-8 -*-

from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, Text, text
from sqlalchemy.orm import relationship

from .base import Base, PGSQL_SCHEMA_UTENTES

class Licencia(Base):
    __tablename__ = 'licencias'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('utentes.licencias_gid_seq'::regclass)"))
    lic_nro = Column(Text, nullable=False, unique=True)
    lic_tipo = Column(Text, nullable=False)
    exploracao = Column(ForeignKey(u'utentes.exploracaos.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    cadastro = Column(Text)
    d_emissao = Column(Date)
    d_validade = Column(Date)
    d_solici = Column(Date)
    estado = Column(Text)
    c_requerid = Column(Numeric(10, 2))
    c_licencia = Column(Numeric(10, 2))
    c_real = Column(Numeric(10, 2))
    c_real_int = Column(Numeric(10, 2))

    exploracao_rel = relationship(u'Exploracao',
                               backref='licencias')

    @staticmethod
    def create_from_json(json):
        l = Licencia()
        l.lic_nro = json.get('lic_nro')
        l.lic_tipo = json.get('lic_tipo')
        l.exploracao = json.get('exploracao')
        l.cadastro = json.get('cadastro')
        l.d_emissao = json.get('l.d_emissao')
        l.d_validade = json.get('d_validade')
        l.d_solici = json.get('d_solici')
        l.estado =  json.get('estado')
        l.c_requerid = json.get('c_requerid')
        l.c_licencia = json.get('c_licencia')
        l.c_real = json.get('c_real')
        l.c_real_int = json.get('c_real_int')
        return l

    def __json__(self, request):
        return {
            'id':self.gid,
            'lic_nro': self.lic_nro,
            'lic_tipo': self.lic_tipo,
            'exploracao': self.exploracao,
            'cadastro': self.cadastro,
            'd_emissao': self.d_emissao,
            'd_validade': self.d_validade,
            'd_solici': self.d_solici,
            'estado': self.estado,
            'c_requerid': self.c_requerid,
            'c_licencia': self.c_licencia,
            'c_real': self.c_real,
            'c_real_int': self.c_real_int
        }

