# -*- coding: utf-8 -*-

ActividadeSchema = {}

ActividadeSchema['Abastecimento'] = [{
  'fieldname': 'tipo',
  'message':   'Tipo da actividade não pode estar vazio',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'Consumo estimado da actividade não tem o formato correcto ou está vazio',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
}, {
  'fieldname': 'habitantes',
  'message':   'O nro de habitantes da actividade não tem o formato correcto ou está vazio',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
}, {
  'fieldname': 'dotacao',
  'message':   'A dotaçâo da actividade não tem o formato correcto ou está vazio',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
}];

ActividadeSchema['Agricultura-Regadia'] = [{
  'fieldname': 'tipo',
  'message':   'Tipo da actividade não pode estar vazio',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'Consumo estimado da actividade não tem o formato correcto ou está vazio',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
},{
  'fieldname': 'cultivos',
  'message':   'A actividade debe ter cultivos',
  'rules':     ['ARRAY_NOT_VOID']
}];

ActividadeSchema['Cultivos'] = [{
  'fieldname': 'c_estimado',
  'message':   'Consumo estimado da actividade não tem o formato correcto ou está vazio',
  'rules':     ['NOT_NULL', 'IS_NUMERIC']
}, {
  'fieldname': 'cultivo',
  'message':   'Tipo de cultivo não pode estar vazio',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'rega',
  'message':   'Tipo de rega não pode estar vazio',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'eficiencia',
  'message':   'Eficiencia não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'area',
  'message':   'Área não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}];

ActividadeSchema['Indústria'] = [{
  'fieldname': 'tipo',
  'message':   'Tipo da actividade não pode estar vazio',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'Consumo estimado da actividade não tem o formato correcto ou está vazio',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
}, {
  'fieldname': 'eval_impac',
  'message':   'Evaluação impacto não tem o formato correcto',
  'rules':     ['IS_BOOLEAN']
}];

ActividadeSchema['Pecuária'] = [{
  'fieldname': 'tipo',
  'message':   'Tipo da actividade não pode estar vazio',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'Consumo estimado da actividade não tem o formato correcto ou está vazio',
  'rules':     ['IS_NUMERIC', 'NOT_NULL']
}, {
  'fieldname': 'reses',
  'message':   'A actividade debe ter reses',
  'rules':     ['ARRAY_NOT_VOID']
}];

ActividadeSchema['Reses'] = [{
  'fieldname': 'c_estimado',
  'message':   'Consumo estimado da actividade não tem o formato correcto ou está vazio',
  'rules':     ['NOT_NULL', 'IS_NUMERIC']
}, {
  'fieldname': 'reses_tipo',
  'message':   'Tipo de reses não pode estar vazio',
  'rules':     ['NOT_NULL']
}, {
  'fieldname': 'reses_nro',
  'message':   'Nro de reses não tem o formato correcto ou está vazio',
  'rules':     ['NOT_NULL', 'IS_NUMERIC']
}, {
  'fieldname': 'c_res',
  'message':   'Consumo por res não tem o formato correcto ou está vazio',
  'rules':     ['NOT_NULL', 'IS_NUMERIC']
}];

ActividadeSchema['Piscicultura'] = [{
  'fieldname': 'tipo',
  'message':   'Tipo da actividade não pode estar vazio',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'Consumo estimado da actividade não tem o formato correcto ou está vazio',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'area',
  'message':   'Área não pode estar vazio',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'v_reservas',
  'message':   'Reservas não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}];

ActividadeSchema['Producção de energia'] = [{
  'fieldname': 'tipo',
  'message':   'Tipo da actividade não pode estar vazio',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'Consumo estimado da actividade não tem o formato correcto ou está vazio',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'alt_agua',
  'message':   'Altura de água não pode estar vazio',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'potencia',
  'message':   'Potência a instalar não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'eval_impac',
  'message':   'Evaluação impacto não tem o formato correcto',
  'rules':     ['IS_BOOLEAN']
}];

ActividadeSchema['Saneamento'] = [{
  'fieldname': 'tipo',
  'message':   'Tipo da actividade não pode estar vazio',
  'rules':     ['NOT_NULL']
},{
  'fieldname': 'c_estimado',
  'message':   'Consumo estimado da actividade não tem o formato correcto ou está vazio',
  'rules':     ['IS_NUMERIC']
}, {
  'fieldname': 'habitantes',
  'message':   'O nro de habitantes da actividade não tem o formato correcto',
  'rules':     ['IS_NUMERIC']
}];
