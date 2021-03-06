# -*- coding: utf-8 -*-

from sqlalchemy import Boolean, Column, Date, Integer, Numeric, Text
from sqlalchemy import ForeignKey, text

from utentes.lib.formatter.formatter import to_decimal, to_date
from utentes.models.base import Base, PGSQL_SCHEMA_UTENTES


class Fonte(Base):
    __tablename__ = 'fontes'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('utentes.fontes_gid_seq'::regclass)"))
    tipo_agua = Column(Text, nullable=False, doc='Tipo de água')
    tipo_fonte = Column(Text, doc='Tipo de Fonte')
    lat_lon = Column(Text, doc='Latitude / Longitud')
    d_dado = Column(Date, doc='Data toma de dados')
    c_soli = Column(Numeric(10, 2), doc='Consumo solicitado')
    c_max = Column(Numeric(10, 2), doc='Máximo caudal extraíble')
    c_real = Column(Numeric(10, 2), doc='Consumo real')
    sist_med = Column(Text, doc='Sistema de medição')
    metodo_est = Column(Text, doc='Método estimação volume')
    observacio = Column(Text, doc='Observações')
    exploracao = Column(
        ForeignKey(
            u'utentes.exploracaos.gid',
            ondelete=u'CASCADE',
            onupdate=u'CASCADE'),
        nullable=False)

    @staticmethod
    def create_from_json(json):
        f = Fonte()
        f.update_from_json(json)
        return f

    def update_from_json(self, json):
        self.gid = json.get('id')
        self.tipo_agua = json.get('tipo_agua')
        self.tipo_fonte = json.get('tipo_fonte')
        self.lat_lon = json.get('lat_lon')
        self.d_dado = to_date(json.get('d_dado'))
        self.c_soli = to_decimal(json.get('c_soli'))
        self.c_max = to_decimal(json.get('c_max'))
        self.c_real = to_decimal(json.get('c_real'))
        self.sist_med = json.get('sist_med')
        self.metodo_est = json.get('metodo_est')
        self.observacio = json.get('observacio')
        # self.exploracao = json.get('exploracao')

    def __json__(self, request):
        return {
            'id': self.gid,
            'tipo_agua': self.tipo_agua,
            'tipo_fonte': self.tipo_fonte,
            'lat_lon': self.lat_lon,
            'd_dado': self.d_dado,
            'c_soli': self.c_soli,
            'c_max': self.c_max,
            'c_real': self.c_real,
            'sist_med': self.sist_med,
            'metodo_est': self.metodo_est,
            'observacio': self.observacio,
            'exploracao': self.exploracao,
        }

    def validate(self, json):
        return []
