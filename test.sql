psql -h localhost -U postgres -d test -c "
UPDATE utentes.exploracaos SET observacio = NULL;
UPDATE utentes.licencias SET estado = 'Irregular' WHERE lic_nro IN ('2015-003-001', '2015-005-001');
UPDATE utentes.licencias SET estado = 'Desconhecido' WHERE lic_nro IN ('2016-033-002', '2016-034-001');
UPDATE utentes.licencias SET estado = 'Não aprovada' WHERE lic_nro IN ('2015-006-001');
UPDATE utentes.licencias SET estado = 'Pendente de solicitação do utente' WHERE lic_nro IN ('2015-007-001');
UPDATE utentes.licencias SET estado = 'Pendente de revisão da solicitação (Direcção)' WHERE lic_nro IN ('2015-008-001');
UPDATE utentes.licencias SET estado = 'Pendente de revisão da solicitação (Chefe DT)' WHERE lic_nro IN ('2015-009-001');
UPDATE utentes.licencias SET estado = 'Pendente de revisão da solicitação (D. Jurídico)' WHERE lic_nro IN ('2015-011-001');
UPDATE utentes.licencias SET estado = 'Pendente de aprovação técnica (Chefe DT)' WHERE lic_nro IN ('2016-019-001');
UPDATE utentes.licencias SET estado = 'Pendente da emisão (D. Jurídico)' WHERE lic_nro IN ('2016-022-001');
UPDATE utentes.licencias SET estado = 'Pendente da firma (Direcção)' WHERE lic_nro IN ('2016-025-001');
"
