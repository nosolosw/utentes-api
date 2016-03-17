# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text, text

from .base import DeclarativeBase, PGSQL_SCHEMA_DOMAINS


class Domain(DeclarativeBase):
    __tablename__ = 'domains'
    __table_args__ = {u'schema': PGSQL_SCHEMA_DOMAINS}

    category = Column(Text, nullable=False, primary_key=True)
    key = Column(Text, nullable=False, primary_key=True)
    value = Column(Text)
    ordering = Column(Text)
    parent = Column(Text, primary_key=True)

    def __json__(self, request):
        return {
            'category': self.category,
            'text':     self.key,
            'alias':    self.value,
            'order':    self.ordering,
            'parent':   self.parent
        }
