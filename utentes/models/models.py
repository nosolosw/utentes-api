# -*- coding: utf-8 -*-

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, Numeric, Text, text
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from shapely.geometry import mapping

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
    the_geom = Column(Geometry('MULTIPOLYGON', '32727'), index=True)

    utente_rel = relationship(u'Utente')

    def __json__(self, request):
        l_sub = [ l for l in self.licencias if l.lic_tipo == 'subterranea' ]
        l_sup = [ l for l in self.licencias if l.lic_tipo == 'superficial' ]

        return {
            'gid': self.gid,
            'exp_name': self.exp_name,
            'exp_id': self.exp_id,
            'utente': self.utente,
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
            # json.dumps(mapping(to_shape(self.geom)))
            'the_geom': mapping(to_shape(self.the_geom)),
            'utente': self.utente_rel,
            'fontes': self.fontes,
            'licencias': {'subterranea': l_sub, 'superficial': l_sup}
        }


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

    def __json__(self, request):
        return {
            'gid':self.gid,
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


class Utente(Base):
    __tablename__ = 'utentes'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('utentes.utentes_gid_seq'::regclass)"))
    nome = Column(Text, nullable=False, unique=True)
    nuit = Column(Text, unique=True)
    entidade = Column(Text)
    reg_comerc = Column(Text)
    reg_zona = Column(Text)

    def __json__(self, request):
        return {
            'gid': self.gid,
            'nome': self.nome,
            'nuit': self.nuit,
            'entidade': self.entidade,
            'reg_comerc': self.reg_comerc,
            'reg_zona': self.reg_zona
            }
