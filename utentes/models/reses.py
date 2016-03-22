# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Numeric, Text
from sqlalchemy import ForeignKey, text

from .base import Base, PGSQL_SCHEMA_UTENTES
from utentes.lib.schema_validator.validator import Validator
import actividades_schema


class ActividadesReses(Base):
    __tablename__ = 'actividades_reses'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('utentes.actividades_reses_gid_seq'::regclass)"))
    actividade = Column(ForeignKey(u'utentes.actividades_pecuaria.gid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    c_estimado = Column(Numeric(10, 2), nullable=False)
    reses_tipo = Column(Text, nullable=False)
    reses_nro = Column(Integer, nullable=False)
    c_res = Column(Integer, nullable=False)
    observacio = Column(Text)

    @staticmethod
    def create_from_json(json):
        res = ActividadesReses()
        res.update_from_json(json)
        return res

    def update_from_json(self, json):
        # actividade - handled by sqlalchemy relationship
        self.gid        = json.get('id')
        self.c_estimado = json.get('c_estimado')
        self.reses_tipo = json.get('reses_tipo')
        self.reses_nro = json.get('reses_nro')
        self.c_res = json.get('c_res')
        self.observacio = json.get('observacio')

    def __json__(self, request):
        json = {c: getattr(self, c) for c in self.__mapper__.columns.keys()}
        del json['gid']
        json['id'] = self.gid
        return json



    def validate(self, json):
        validator = Validator(ActividadeSchema['Reses'])
        return validator.validate(json)
