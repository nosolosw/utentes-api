# -*- coding: utf-8 -*-

ActividadesProduccaoEnergia_SCHEMA = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message': 'c_estimado não tem o formato correcto',
  'rules': ['IS_NUMERIC']
}, {
  'fieldname': 'alt_agua',
  'message':   'alt_agua non pode estar vacío',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'potencia',
  'message':   'potencia não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}];

ActividadesSaneamento_SCHEMA = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'habitantes',
  'message':   'habitantes não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}];

ActividadesAbastecemento_SCHEMA = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
}, {
  'fieldname': 'habitantes',
  'message':   'habitantes não tem o formato correcto',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
}, {
  'fieldname': 'dotacao',
  'message':   'dotacao não tem o formato correcto',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
}];

ActividadesIndustria_SCHEMA = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}];

ActividadesIndustria_SCHEMA = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
}];
