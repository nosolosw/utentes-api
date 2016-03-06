# -*- coding: utf-8 -*-

EXPLORACAO_SCHEMA = [{
  'fieldname': 'exp_id',
  'message':   'Nº de exploracão non pode estar vacío',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'exp_id',
  'message': 'O Nº de exploracão não tem o formato correcto',
  'rules': ['EXP_ID_FORMAT']
}, {
  'fieldname': 'exp_name',
  'message':   'Nome da exploracão non pode estar vacío',
  'rules':     ['NOT_NULL']
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
  'fieldname': 'utente',
  'message':   'A exploracão ten que ter asignado un utente',
  'rules':     ['NOT_NULL']
}];
