# -*- coding: utf-8 -*-

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, Numeric, Text, text
from sqlalchemy.orm import relationship

from .base import Base, PGSQL_SCHEMA_UTENTES

class Fonte(Base):
    __tablename__ = 'fontes'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('utentes.fontes_gid_seq'::regclass)"))
    exploracao = Column(ForeignKey(u'utentes.exploracaos.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    tipo_agua = Column(Text, nullable=False)
    tipo_fonte = Column(Text)
    lat_lon = Column(Text)
    d_dado = Column(Date)
    c_requerid = Column(Numeric(10, 2))
    c_max = Column(Numeric(10, 2))
    c_real = Column(Numeric(10, 2))
    contador = Column(Boolean)
    metodo_est = Column(Text)

    exploracao_rel = relationship(u'Exploracao',
                               backref='fontes')

    @staticmethod
    def create_from_json(json):
        f = Fonte()
        f.exploracao = json.get('exploracao')
        f.tipo_agua = json.get('tipo_agua')
        f.tipo_fonte = json.get('tipo_fonte')
        f.lat_lon = json.get('lat_lon')
        f.d_dado = json.get('d_dado')
        f.c_requerid = json.get('c_requerid')
        f.c_max =  json.get('c_max')
        f.c_real = json.get('c_real')
        f.contador = json.get('contador')
        f.metodo_est = json.get('metodo_est')
        return f

    def __json__(self, request):
        return {
            'gid': self.gid,
            'exploracao': self.exploracao,
            'tipo_agua': self.tipo_agua,
            'tipo_fonte': self.tipo_fonte,
            'lat_lon': self.lat_lon,
            'd_dado': self.d_dado,
            'c_requerid': self.c_requerid,
            'c_max': self.c_max,
            'c_real': self.c_real,
            'contador': self.contador,
            'metodo_est': self.metodo_est
        }