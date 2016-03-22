# -*- coding: utf-8 -*-

FONTE_SCHEMA = [{
  'fieldname': 'tipo_agua',
  'message':   'tipo_agua não tem o formato correcto',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'd_dado',
  'message':   'd_dado não tem o formato correcto',
  'rules':     ['IS_DATE']
}, {
  'fieldname': 'c_soli',
  'message':   'c_soli não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'c_max',
  'message':   'c_max não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'c_real',
  'message':   'c_real_fon não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}];
