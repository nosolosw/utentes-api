# -*- coding: utf-8 -*-

from sqlalchemy import Boolean, Column, Integer, Date, Numeric, Text
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import relationship

from utentes.models.base import (
    Base,
    PGSQL_SCHEMA_UTENTES,
    update_array,
)
from utentes.lib.schema_validator.validator import Validator
import actividades_schema
from utentes.models.cultivo import ActividadesCultivos
from utentes.models.reses import ActividadesReses



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
        'polymorphic_identity': 'actividades',
        'polymorphic_on': tipo
    }

    # def validate(self, json):
    #     validator_name = self.__class__.__name__ + '_SCHEMA'
    #     validator = Validator(actividades_schema.validator_name)
    #     return validator.validate(json)

    @staticmethod
    def create_from_json(json):
        classes = {
            u'Abastecimento': ActividadesAbastecemento,
            u'Agricultura-Regadia': ActividadesAgriculturaRega,
            u'Indústria': ActividadesIndustria,
            u'Pecuária': ActividadesPecuaria,
            u'Piscicultura': ActividadesPiscicultura,
            u'Producção de energia': ActividadesProduccaoEnergia,
            u'Saneamento': ActividadesSaneamento,
        }
        tipo = json.get('tipo')
        a = classes[tipo]()
        a.update_from_json(json)
        return a

    def __json__(self, request):
        json = {c: getattr(self, c) for c in self.__mapper__.columns.keys()}
        del json['gid']
        json['id'] = self.gid
        return json

class ActividadesAbastecemento(Actividade):
    __tablename__ = 'actividades_abastecemento'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2), nullable=False)
    habitantes = Column(Integer, nullable=False, server_default=text("20"))
    dotacao = Column(Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': u'Abastecimento',
    }

    def update_from_json(self, json):
        self.gid = json.get('id')
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        self.habitantes = json.get('habitantes')
        self.dotacao = json.get('dotacao')

    def validate(self, json):
        validator = Validator(actividades_schema.ActividadesAbastecemento_SCHEMA)
        return validator.validate(json)

class ActividadesAgriculturaRega(Actividade):
    __tablename__ = 'actividades_agricultura_rega'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': u'Agricultura-Regadia',
    }

    cultivos  = relationship('ActividadesCultivos',
                              cascade="all, delete-orphan",
                              order_by='ActividadesCultivos.gid',
                              passive_deletes=True)

    def __json__(self, request):
        json = {c: getattr(self, c) for c in self.__mapper__.columns.keys()}
        del json['gid']
        json['id'] = self.gid
        json['cultivos'] = {
            'type': 'FeatureCollection',
            'features': self.cultivos
        }
        return json

    def update_from_json(self, json):
        self.gid = json.get('id')
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        update_array(self.cultivos,
                    json.get('cultivos'),
                    ActividadesCultivos.create_from_json)

    def validate(self, json):
        validator = Validator(actividades_schema.ActividadesAgriculturaRega_SCHEMA)
        return validator.validate(json)


class ActividadesIndustria(Actividade):
    __tablename__ = 'actividades_industria'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2))
    # tipo_indus = Column(ForeignKey(u'domains.industria_tipo.key', onupdate=u'CASCADE'))
    tipo_indus = Column(Text)
    instalacio = Column(Text)
    efluente   = Column(Text)
    tratamento = Column(Text)
    eval_impac = Column(Boolean)

    __mapper_args__ = {
        'polymorphic_identity': u'Indústria',
    }

    def update_from_json(self, json):
        self.gid = json.get('id')
        self.tipo       = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        self.tipo_indus = json.get('tipo_indus')
        self.instalacio  = json.get('instalacio')
        self.efluente   = json.get('efluente')
        self.tratamento = json.get('tratamento')
        self.eval_impac = json.get('eval_impac')

    def validate(self, json):
        validator = Validator(actividades_schema.ActividadesIndustria_SCHEMA)
        return validator.validate(json)

class ActividadesPecuaria(Actividade):
    __tablename__ = 'actividades_pecuaria'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': u'Pecuária',
    }

    reses  = relationship('ActividadesReses',
                        cascade="all, delete-orphan",
                        order_by='ActividadesReses.gid',
                        passive_deletes=True)

    def __json__(self, request):
        json = {c: getattr(self, c) for c in self.__mapper__.columns.keys()}
        del json['gid']
        json['id'] = self.gid
        json['reses'] = self.reses
        return json

    def update_from_json(self, json):
        self.gid = json.get('id')
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        update_array(self.reses,
                     json.get('reses'),
                     ActividadesReses.create_from_json)

    def validate(self, json):
        validator = Validator(actividades_schema.ActividadesPecuaria_SCHEMA)
        return validator.validate(json)

class ActividadesPiscicultura(Actividade):
    __tablename__ = 'actividades_piscicultura'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2))
    area = Column(Numeric(10, 2))
    v_reservas = Column(Numeric(10, 2))

    __mapper_args__ = {
        'polymorphic_identity': u'Piscicultura',
    }

    def update_from_json(self, json):
        self.gid = json.get('id')
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        self.area = json.get('area')
        self.v_reservas = json.get('v_reservas')

    def validate(self, json):
        validator = Validator(actividades_schema.ActividadesPiscicultura_SCHEMA)
        return validator.validate(json)

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
        'polymorphic_identity': u'Producção de energia',
    }

    def update_from_json(self, json):
        self.gid = json.get('id')
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        self.energia_tipo = json.get('energia_tipo')
        self.alt_agua = json.get('alt_agua')
        self.potencia = json.get('potencia')
        self.equipo = json.get('equipo')
        self.eval_impac = json.get('eval_impac')

    def validate(self, json):
        validator = Validator(actividades_schema.ActividadesProduccaoEnergia_SCHEMA)
        return validator.validate(json)


class ActividadesSaneamento(Actividade):
    __tablename__ = 'actividades_saneamento'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(ForeignKey(u'utentes.actividades.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    c_estimado = Column(Numeric(10, 2))
    habitantes = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': u'Saneamento',
    }

    def update_from_json(self, json):
        self.gid = json.get('id')
        self.tipo = json.get('tipo')
        self.c_estimado = json.get('c_estimado')
        self.habitantes = json.get('habitantes')

    def validate(self, json):
        validator = Validator(actividades_schema.ActividadesSaneamento_SCHEMA)
        return validator.validate(json)
