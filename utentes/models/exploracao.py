# -*- coding: utf-8 -*-

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Date, Numeric, Text, text
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from utentes.models.fonte import Fonte
from utentes.models.licencia import Licencia

from .base import Base, PGSQL_SCHEMA_UTENTES

class Exploracao(Base):
    __tablename__ = 'exploracaos'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid        = Column(Integer, primary_key=True, server_default=text("nextval('utentes.exploracaos_gid_seq'::regclass)"))
    exp_id     = Column(Text, nullable=False, unique=True)
    exp_name   = Column(Text, nullable=False)
    observacio = Column(Text)
    d_soli     = Column(Date)
    loc_provin = Column(Text, nullable=False)
    loc_distri = Column(Text, nullable=False)
    loc_posto  = Column(Text, nullable=False)
    loc_nucleo = Column(Text)
    loc_endere = Column(Text)
    loc_bacia  = Column(Text)
    loc_subaci = Column(Text)
    loc_rio    = Column(Text)
    pagos      = Column(Boolean)
    c_soli     = Column(Numeric(10, 2))
    c_licencia = Column(Numeric(10, 2))
    c_real     = Column(Numeric(10, 2))
    c_estimado = Column(Numeric(10, 2))
    actividade = Column(Text)
    area       = Column(Numeric(10, 2))
    the_geom   = Column(Geometry('MULTIPOLYGON', '32737'), index=True)
    utente     = Column(ForeignKey(u'utentes.utentes.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)

    utente_rel = relationship(u'Utente')

    @staticmethod
    def create_from_json(body):
        e = Exploracao()
        mandatory  = [f for f in e.__table__.c if not f.nullable]
        e.exp_id     = json.get('exp_id')
        e.exp_name   = json.get('exp_name')
        e.d_soli     = json.get('d_soli')
        e.observacio = json.get('observacio')
        e.loc_provin = json.get('loc_provin')
        e.loc_distri = json.get('loc_distri')
        e.loc_posto  = json.get('loc_posto')
        e.loc_nucleo = json.get('loc_nucleo')
        e.loc_endere = json.get('loc_endere')
        e.loc_bacia  = json.get('loc_bacia')
        e.loc_subaci = json.get('loc_subaci')
        e.loc_rio    = json.get('loc_rio')
        e.pagos      = json.get('pagos')
        e.c_soli     = json.get('c_soli')
        e.c_licencia = json.get('c_licencia')
        e.c_real     = json.get('c_real')
        e.c_estimado = json.get('c_estimado')
        e.actividade = json.get('actividade')

        geom = body.get('the_geom')
        if geom:
            from geoalchemy2.elements import WKTElement
            from utentes.geomet import wkt
            e.the_geom = WKTElement(wkt.dumps(geom), srid=32737)

        # e.utente     = json.get('utente')
        # e.utente_rel = json.get('utente')

        e.fontes = e.fontes or []
        for f in body.get('fontes'):
            e.fontes.append(Fonte.create_from_json(f))
        e.licencias = []
        for l in body.get('licencias'):
            e.licencias.append(Licencia.create_from_json(l))

        return e

    def __json__(self, request):
        the_geom = None
        if self.the_geom is not None:
            import json
            the_geom = json.loads(request.db.query(self.the_geom.ST_Transform(4326).ST_AsGeoJSON()).first()[0])
        return {
            'type': 'Feature',
            'properties': {
                'id':         self.gid,
                'exp_id':     self.exp_id,
                'exp_name':   self.exp_name,
                'd_soli':     self.d_soli,
                'observacio': self.observacio,
                'loc_provin': self.loc_provin,
                'loc_distri': self.loc_distri,
                'loc_posto':  self.loc_posto,
                'loc_nucleo': self.loc_nucleo,
                'loc_endere': self.loc_endere,
                'loc_bacia':  self.loc_bacia,
                'loc_subaci': self.loc_subaci,
                'loc_rio':    self.loc_rio,
                'pagos':      self.pagos,
                'c_soli':     self.c_soli,
                'c_licencia': self.c_licencia,
                'c_real':     self.c_real,
                'c_estimado': self.c_estimado,
                'actividade': self.actividade,
                #'utente':     self.utente,
                'area':       self.area,
                'utente':     self.utente_rel,
                'fontes':     self.fontes,
                'licencias':  self.licencias,
            },
            'geometry': the_geom
        }
