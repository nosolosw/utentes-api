# -*- coding: utf-8 -*-

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

ActividadesAgriculturaRega_SCHEMA = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
},{
  'fieldname': 'cultivos',
  'message':   'cultivos non pode estar vacío',
  'rules':     ['NOT_NULL']
}];

ActividadesCultivos_SCHEMA = [{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['NOT_NULL', 'IS_NUMERIC']
}, {
  'fieldname': 'cultivo',
  'message':   'cultivo non pode estar vacío',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'rega',
  'message':   'rega non pode estar vacío',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'eficiencia',
  'message':   'eficiencia non pode estar vacío',
  'rules':     ['NOT_NULL', 'IS_NUMERIC']
}, {
  'fieldname': 'area',
  'message':   'area non pode estar vacío',
  'rules':     ['NOT_NULL', 'IS_NUMERIC']
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

ActividadesPecuaria_SCHEMA = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'reses',
  'message':   'reses non pode estar vacío',
  'rules':     ['NOT_NULL']
}];

ActividadesReses_SCHEMA = [{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['NOT_NULL', 'IS_NUMERIC']
}, {
  'fieldname': 'reses_tipo',
  'message':   'reses_tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'reses_nro',
  'message':   'reses_nro non pode estar vacío',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'c_res',
  'message':   'c_res non pode estar vacío',
  'rules':     ['NOT_NULL', 'IS_NUMERIC']
}];

ActividadesPiscicultura_SCHEMA = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message': 'c_estimado não tem o formato correcto',
  'rules': ['IS_NUMERIC']
}, {
  'fieldname': 'area',
  'message':   'area non pode estar vacío',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'v_reservas',
  'message':   'v_reservas não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}];

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
