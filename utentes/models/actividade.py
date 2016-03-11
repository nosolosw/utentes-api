# -*- coding: utf-8 -*-

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Date, Numeric, Text, text
from sqlalchemy.orm import relationship

from .base import Base, PGSQL_SCHEMA_UTENTES

class Actividade(Base):
    __tablename__ = 'actividades'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('utentes.actividades_gid_seq'::regclass)"))
    exploracao = Column(ForeignKey(u'utentes.exploracaos.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    tipo = Column(ForeignKey(u'domains.actividade.key', onupdate=u'CASCADE'), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity':'actividades',
        'polymorphic_on':tipo
    }

    def __json__(self, request):
        return {c: getattr(self, c) for c in self.__table__.columns.keys()}


class ActividadesProduccaoEnergia(Actividade):
    __tablename__ = 'actividades_produccao_energia'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2))
    energia_tipo = Column(ForeignKey(u'domains.energia_tipo.key', onupdate=u'CASCADE'))
    alt_agua = Column(Numeric(10, 2))
    potencia = Column(Numeric(10, 2))
    equipo = Column(Text)
    eval_impac = Column(Boolean)

    __mapper_args__ = {
        'polymorphic_identity':u'Producção de energia',
    }


class ActividadesSaneamento(Actividade):
    __tablename__ = 'actividades_saneamento'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2))
    habitantes = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':u'Saneamento',
    }


class ActividadesAbastecemento(Actividade):
    __tablename__ = 'actividades_abastecemento'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2), nullable=False)
    habitantes = Column(Integer, nullable=False, server_default=text("20"))
    dotacao = Column(Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity':u'Abastecimento',
    }


class ActividadesPiscicultura(Actividade):
    __tablename__ = 'actividades_piscicultura'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2))
    area = Column(Numeric(10, 2))
    v_reservas = Column(Numeric(10, 2))

    __mapper_args__ = {
        'polymorphic_identity':u'Piscicultura',
    }


class ActividadesIndustria(Actividade):
    __tablename__ = 'actividades_industria'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2))
    industria_tipo = Column(ForeignKey(u'domains.industria_tipo.key', onupdate=u'CASCADE'))
    instalacio = Column(Text)
    efluente = Column(Text)
    tratamento = Column(Text)
    eval_impac = Column(Boolean)

    __mapper_args__ = {
        'polymorphic_identity':u'Indústria',
    }


class ActividadesAgriculturaRega(Actividade):
    __tablename__ = 'actividades_agricultura_rega'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity':u'Agricultura-Regadia',
    }
