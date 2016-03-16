# -*- coding: utf-8 -*-

EXPLORACAO_SCHEMA = [{
  'fieldname': 'exp_id',
  'message':   'Nro de exploracão non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'exp_id',
  'message': 'Nro de exploracão não tem o formato correcto',
  'rules': ['EXP_ID_FORMAT']
}, {
  'fieldname': 'exp_name',
  'message':   'Nome da exploracão non pode estar vacío',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'd_soli',
  'message':   'Data de solicitação não tem o formato correcto',
  'rules':     ['IS_DATE']
}, {
  'fieldname': 'loc_provin',
  'message':   'A provincia da exploracão non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'loc_distri',
  'message':   'O distrito da exploracão non pode estar vacío',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'loc_posto',
  'message':   'O posto da exploracão non pode estar vacío',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'c_soli',
  'message':   'Consumo solicitado não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'c_licencia',
  'message':   'Consumo licencia não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'c_real',
  'message':   'Consumo real não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'c_estimado',
  'message':   'Consumo estimado não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'area',
  'message':   'Área não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'utente',
  'message':   'A exploracão ten que ter asignado un utente',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'pagos',
  'message':   'Pagos não tem o formato correcto',
  'rules':     ['IS_BOOLEAN']
}];
