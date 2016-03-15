# -*- coding: utf-8 -*-

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Date, Numeric, Text, text
from sqlalchemy.orm import relationship

from .base import Base, PGSQL_SCHEMA_UTENTES

class Actividade(Base):
    __tablename__ = 'actividades'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('utentes.actividades_gid_seq'::regclass)"))
    exploracao = Column(ForeignKey(u'utentes.exploracaos.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    # when updating tipo value, or other ForeignKey with tables not defined in the mapper
    # an exception is raised. Probably removing onupdate will work
    # tipo = Column(ForeignKey(u'domains.actividade.key', onupdate=u'CASCADE'), nullable=False)
    tipo = Column(Text, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity':'actividades',
        'polymorphic_on':tipo
    }

    @staticmethod
    def create_from_json(json):
        classes = {
            u'Producção de energia': ActividadesProduccaoEnergia,
            u'Saneamento': ActividadesSaneamento,
            u'Abastecimento': ActividadesAbastecemento,
            u'Piscicultura': ActividadesPiscicultura,
            u'Indústria': ActividadesIndustria,
            u'Agricultura-Regadia': ActividadesAgriculturaRega
        }
        tipo = json.get(tipo)
        print tipo
        a = classes[tipo]()
        print a
        a.update_from_json(json)
        return a

    def __json__(self, request):
        json = {c: getattr(self, c) for c in self.__table__.columns.keys()}
        json['tipo'] = self.tipo
        return json


class ActividadesProduccaoEnergia(Actividade):
    __tablename__ = 'actividades_produccao_energia'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2))
    # energia_tipo = Column(ForeignKey(u'domains.energia_tipo.key', onupdate=u'CASCADE'))
    energia_tipo = Column(Text)
    alt_agua = Column(Numeric(10, 2))
    potencia = Column(Numeric(10, 2))
    equipo = Column(Text)
    eval_impac = Column(Boolean)

    __mapper_args__ = {
        'polymorphic_identity':u'Producção de energia',
    }

    def update_from_json(self, json):
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        self.energia_tipo = json.get('energia_tipo')
        self.alt_agua = json.get('alt_agua')
        self.potencia = json.get('potencia')
        self.equipo = json.get('equipo')
        self.eval_impac = json.eval_impac('eval_impac')




class ActividadesSaneamento(Actividade):
    __tablename__ = 'actividades_saneamento'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2))
    habitantes = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':u'Saneamento',
    }

    def update_from_json(self, json):
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        self.habitanes = json.get('habitantes')


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

    def update_from_json(self, json):
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        self.habitantes = json.get('habitantes')
        self.dotacao = json.get('dotacao')


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

    def update_from_json(self, json):
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        self.area = json.get('area')
        self.v_reservas = json.get('v_reservas')


class ActividadesIndustria(Actividade):
    __tablename__ = 'actividades_industria'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2))
    # industria_tipo = Column(ForeignKey(u'domains.industria_tipo.key', onupdate=u'CASCADE'))
    industria_tipo = Column(Text)
    instalacio = Column(Text)
    efluente = Column(Text)
    tratamento = Column(Text)
    eval_impac = Column(Boolean)

    __mapper_args__ = {
        'polymorphic_identity':u'Indústria',
    }

    def update_from_json(self, json):
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        self.industria_tipo = json.get('industria_tipo')
        self.intalacio = json.get('instalacio')
        self.efluente = json.get('efluente')
        self.tratamento = json.get('tratamento')
        self.eval_impac = json.get('eval_impac')


class ActividadesAgriculturaRega(Actividade):
    __tablename__ = 'actividades_agricultura_rega'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity':u'Agricultura-Regadia',
    }

    def update_from_json(self, json):
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
