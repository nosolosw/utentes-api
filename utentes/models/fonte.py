# -*- coding: utf-8 -*-

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, Numeric, Text, text
from sqlalchemy.orm import relationship

from .base import Base, PGSQL_SCHEMA_UTENTES

class Fonte(Base):
    __tablename__ = 'fontes'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid        = Column(Integer, primary_key=True, server_default=text("nextval('utentes.fontes_gid_seq'::regclass)"))
    tipo_agua  = Column(Text, nullable=False)
    tipo_fonte = Column(Text)
    lat_lon    = Column(Text)
    d_dado     = Column(Date)
    c_soli     = Column(Numeric(10, 2))
    c_max      = Column(Numeric(10, 2))
    c_real     = Column(Numeric(10, 2))
    contador   = Column(Boolean)
    metodo_est = Column(Text)
    observacio = Column(Text)
    exploracao = Column(ForeignKey(u'utentes.exploracaos.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)

    exploracao_rel = relationship(u'Exploracao',
                               backref='fontes')

    @staticmethod
    def create_from_json(json):
        f = Fonte()
        f.update_from_json(json)
        return f

    def update_from_json(self, json):
        self.tipo_agua  = json.get('tipo_agua')
        self.tipo_fonte = json.get('tipo_fonte')
        self.lat_lon    = json.get('lat_lon')
        self.d_dado     = json.get('d_dado')
        self.c_soli     = json.get('c_soli')
        self.c_max      = json.get('c_max')
        self.c_real     = json.get('c_real')
        self.contador   = json.get('contador')
        self.metodo_est = json.get('metodo_est')
        self.observacio = json.get('observacio')
        self.exploracao = json.get('exploracao')


    def __json__(self, request):
        return {
            'id':         self.gid,
            'tipo_agua':  self.tipo_agua,
            'tipo_fonte': self.tipo_fonte,
            'lat_lon':    self.lat_lon,
            'd_dado':     self.d_dado,
            'c_soli':     self.c_soli,
            'c_max':      self.c_max,
            'c_real':     self.c_real,
            'contador':   self.contador,
            'metodo_est': self.metodo_est,
            'observacio': self.observacio,
            'exploracao': self.exploracao,
        }
