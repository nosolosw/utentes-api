# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    Integer,
    Text,
    )

from .base import Base, PGSQL_SCHEMA_UTENTES

class MyModel(Base):
    __tablename__ = 'spatial_ref_sys'
    __table_args__ = {'schema': 'public'}

    srid = Column(Integer, primary_key=True, doc='SRID')
    auth_name = Column(Text, doc='Authority name')
    auth_srid = Column(Integer, doc='Authority srid')
    srtext = Column(Text, doc='srtext')
    proj4text = Column(Text, doc='proj4text')

    def __json__(self, request):
        return {
            'srid': self.srid,
            'auth_name': self.auth_name,
            'auth_srid': self.auth_srid,
            'srtext': self.srtext,
            'proj4text': self.proj4text
        }
