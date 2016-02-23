# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text, text
from .base import Base, PGSQL_SCHEMA_UTENTES

class Domain(Base):
    __tablename__ = 'domains'
    __table_args__ = {u'schema': PGSQL_SCHEMA_UTENTES}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('utentes.domains_gid_seq'::regclass)"))
    category = Column(Text, nullable=False)
    value = Column(Text, nullable=False)
    alias = Column(Text)
    ordering = Column(Integer)
    parent = Column(Text)

    def __json__(self, request):
        return {
            'category': self.category,
            'text': self.value,
            'alias': self.alias,
            'order': self.ordering,
            'parent': self.parent
        }
