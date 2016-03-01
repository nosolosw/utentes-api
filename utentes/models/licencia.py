# -*- coding: utf-8 -*-

from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, Text, text
from sqlalchemy.orm import relationship

from .base import Base, PGSQL_SCHEMA_UTENTES

class Licencia(Base):
    __tablename__ = 'licencias'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid        = Column(Integer, primary_key=True, server_default=text("nextval('utentes.licencias_gid_seq'::regclass)"))
    lic_nro    = Column(Text, nullable=False, unique=True)
    lic_tipo   = Column(Text, nullable=False)
    finalidade = Column(Text)
    cadastro   = Column(Text)
    estado     = Column(Text)
    d_emissao  = Column(Date)
    d_validade = Column(Date)
    c_soli_tot = Column(Numeric(10, 2))
    c_soli_int = Column(Numeric(10, 2))
    c_soli_fon = Column(Numeric(10, 2))
    c_licencia = Column(Numeric(10, 2))
    c_real_tot = Column(Numeric(10, 2))
    c_real_int = Column(Numeric(10, 2))
    c_real_fon = Column(Numeric(10, 2))
    exploracao = Column(ForeignKey(u'utentes.exploracaos.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)

    exploracao_rel = relationship(u'Exploracao',
                               backref='licencias')

    @staticmethod
    def create_from_json(json):
        l = Licencia()
        l.lic_nro    = json.get('lic_nro')
        l.lic_tipo   = json.get('lic_tipo')
        l.finalidade = json.get('finalidade')
        l.cadastro   = json.get('cadastro')
        l.estado     = json.get('estado')
        l.d_emissao  = json.get('l.d_emissao')
        l.d_validade = json.get('d_validade')
        l.c_soli_tot = json.get('c_soli_tot')
        l.c_soli_int = json.get('c_soli_int')
        l.c_soli_fon = json.get('c_soli_fon')
        l.c_licencia = json.get('c_licencia')
        l.c_real_tot = json.get('c_real_tot')
        l.c_real_int = json.get('c_real_int')
        l.c_real_fon = json.get('c_real_fon')
        l.exploracao = json.get('exploracao')
        return l

    def __json__(self, request):
        return {
            'id':         self.gid,
            'lic_nro':    self.lic_nro,
            'lic_tipo':   self.lic_tipo,
            'finalidade': self.finalidade,
            'cadastro':   self.cadastro,
            'estado':     self.estado,
            'd_emissao':  self.d_emissao,
            'd_validade': self.d_validade,
            'c_soli_tot': self.c_soli_tot,
            'c_soli_int': self.c_soli_int,
            'c_soli_fon': self.c_soli_fon,
            'c_licencia': self.c_licencia,
            'c_real_tot': self.c_real_tot,
            'c_real_int': self.c_real_int,
            'c_real_fon': self.c_real_fon,
            'exploracao': self.exploracao,
        }
