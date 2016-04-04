# -*- coding: utf-8 -*-

ActividadeSchema = {}

ActividadeSchema['Abastecimento'] = [{
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
}]

ActividadeSchema['Agricultura-Regadia'] = [{
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
}]

ActividadeSchema['Cultivos'] = [{
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
  'message':   'area não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}]

ActividadeSchema['Indústria'] = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'eval_impac',
  'message':   'eval_impac não tem o formato correcto',
  'rules':     ['IS_BOOLEAN']
}]

ActividadeSchema['Pecuária'] = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
}, {
  'fieldname': 'reses',
  'message':   'reses non pode estar vacío',
  'rules':     ['NOT_NULL']
}]

ActividadeSchema['Reses'] = [{
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
  'rules':     ['NOT_NULL', 'IS_NUMERIC']
}, {
  'fieldname': 'c_res',
  'message':   'c_res non pode estar vacío',
  'rules':     ['NOT_NULL', 'IS_NUMERIC']
}]

ActividadeSchema['Piscicultura'] = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'area',
  'message':   'area non pode estar vacío',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'v_reservas',
  'message':   'v_reservas não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}]

ActividadeSchema['Producção de energia'] = [{
  'fieldname': 'tipo',
  'message':   'tipo non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'c_estimado não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'alt_agua',
  'message':   'alt_agua non pode estar vacío',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'potencia',
  'message':   'potencia não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'eval_impac',
  'message':   'eval_impac não tem o formato correcto',
  'rules':     ['IS_BOOLEAN']
}]

ActividadeSchema['Saneamento'] = [{
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
}]
