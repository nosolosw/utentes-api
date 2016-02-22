# -*- coding: utf-8 -*-

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric, Text, text
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import mapping, shape

from utentes.models.fonte import Fonte
from utentes.models.licencia import Licencia

from .base import Base, PGSQL_SCHEMA_UTENTES

class Exploracao(Base):
    __tablename__ = 'exploracaos'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('utentes.exploracaos_gid_seq'::regclass)"))
    exp_name = Column(Text, nullable=False, unique=True)
    exp_id = Column(Text, nullable=False, unique=True)
    utente = Column(ForeignKey(u'utentes.utentes.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    observacio = Column(Text)
    loc_provin = Column(Text, nullable=False)
    loc_distri = Column(Text, nullable=False)
    loc_posto = Column(Text, nullable=False)
    loc_nucleo = Column(Text)
    loc_endere = Column(Text)
    loc_bacia = Column(Text)
    loc_rio = Column(Text)
    pagos = Column(Boolean, nullable=False)
    c_requerid = Column(Numeric(10, 2))
    c_licencia = Column(Numeric(10, 2))
    c_real = Column(Numeric(10, 2))
    c_estimado = Column(Numeric(10, 2))
    the_geom = Column(Geometry('MULTIPOLYGON', '32737'), index=True)

    utente_rel = relationship(u'Utente')

    @staticmethod
    def create_from_json(json):
        e = Exploracao()
        mandatory = [f for f in e.__table__.c if not f.nullable]
        e.exp_name = json.get('exp_name')
        e.exp_id = json.get('exp_id')
        # e.utente = json.get('utente')
        e.observacio = json.get('observacio')
        e.loc_provin = json.get('loc_provin')
        e.loc_distri = json.get('loc_distri')
        e.loc_posto =  json.get('loc_posto')
        e.loc_nucleo = json.get('loc_nucleo')
        e.loc_endere = json.get('loc_endere')
        e.loc_bacia = json.get('loc_bacia')
        e.loc_rio = json.get('loc_rio')
        e.pagos = json.get('pagos')
        e.c_requerid = json.get('c_requerid')
        e.c_licencia = json.get('c_licencia')
        e.c_real = json.get('c_real')
        e.c_estimado = json.get('c_estimado')
        geom = json.get('the_geom')
        if geom:
            e.the_geom = from_shape(shape(), srid=32737)
        # e.utente_rel = json.get('utente')
        e.fontes = e.fontes or []
        for f in json.get('fontes'):
            e.fontes.append(Fonte.create_from_json(f))
        e.licencias = []
        for l in json.get('licencias'):
            e.licencias.append(Licencia.create_from_json(l))
        return e

    def __json__(self, request):
        return {
            'gid': self.gid,
            'exp_name': self.exp_name,
            'exp_id': self.exp_id,
            # 'utente': self.utente,
            'observacio': self.observacio,
            'loc_provin': self.loc_provin,
            'loc_distri': self.loc_distri,
            'loc_posto': self.loc_posto,
            'loc_nucleo': self.loc_nucleo,
            'loc_endere': self.loc_endere,
            'loc_bacia': self.loc_bacia,
            'loc_rio': self.loc_rio,
            'pagos': self.pagos,
            'c_requerid': self.c_requerid,
            'c_licencia': self.c_licencia,
            'c_real': self.c_real,
            'c_estimado': self.c_estimado,
            'the_geom': mapping(to_shape(self.the_geom)) if self.the_geom else '',
            'utente': self.utente_rel,
            'fontes': self.fontes,
            'licencias': self.licencias
        }
