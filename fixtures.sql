
delete from utentes.utentes;
insert into utentes.utentes (nome, nuit, entidade, reg_comerc, reg_zona) VALUES ('utente1', 'nuit_utente1', 'entidade_utente1', 'reg_comerc_utente1', 'reg_zon_utente1');
insert into utentes.utentes (nome) VALUES ('utente21');

delete from utentes.exploracaos;

insert into utentes.exploracaos
       (exp_name, exp_id, utente, observacio, loc_provin, loc_distri, loc_posto, loc_nucleo, loc_endere, loc_bacia, loc_rio, pagos, c_requerid, c_licencia, c_real, c_estimado, the_geom)
       VALUES
       ('exploracao1', 'id_exploracao1',
       (SELECT gid from utentes.utentes WHERE nome = 'utente1'),
       'una observación importante', 'loc_provin_1', 'loc_distri_1', 'loc_posto_1', 'loc_nucleo_1', 'loc_endere_1', 'loc_bacia_1', 'loc_rio_1', true, 12.34, 45.11, 0, 444,

       st_geomfromtext('MULTIPOLYGON( ((1 1, 1 2, 2 2, 2 1, 1 1)), (( 3 3, 3 4, 4 4, 4 3, 3 3 )) )',32737)
);

insert into utentes.exploracaos (exp_name, exp_id, utente, loc_provin, loc_distri, loc_posto, pagos) VALUES ('exploracao2', 'id_exploracao2', (SELECT gid from utentes.utentes WHERE nome = 'utente1'), 'loc_provin_2', 'loc_distri_2', 'loc_posto_2', false);


insert into utentes.fontes (exploracao, tipo_agua, tipo_fonte, lat_lon, d_dado, c_requerid, c_max, c_real, contador, metodo_est) VALUES ((SELECT gid FROM utentes.exploracaos WHERE exp_id='id_exploracao1'), 'tipo_agua_1', 'tipo_fonte1', 'lat_lon_1', now(), 11.44, 12, 24.5, true, 'metodo_est');

insert into utentes.fontes (exploracao, tipo_agua, tipo_fonte, lat_lon, d_dado, c_requerid, c_max, c_real, contador, metodo_est) VALUES ((SELECT gid FROM utentes.exploracaos WHERE exp_id='id_exploracao1'), 'tipo_agua_2', 'tipo_fonte2', 'lat_lon_2', now(), 11.44, 12, 24.5, false, 'metodo_est2');

insert into utentes.licencias (lic_nro, lic_tipo, exploracao, cadastro, d_emissao, d_validade, d_solici, estado, c_requerid, c_licencia, c_real, c_real_int) VALUES ('lic_nro_1', 'subterranea', (SELECT gid FROM utentes.exploracaos WHERE exp_id='id_exploracao1'), 'cadastro1', now(), now(), now(), 'estado1', 1, 2, 3, 4);

insert into utentes.licencias (lic_nro, lic_tipo, exploracao, cadastro, d_emissao, d_validade, d_solici, estado, c_requerid, c_licencia, c_real, c_real_int) VALUES ('lic_nro_2', 'superficial', (SELECT gid FROM utentes.exploracaos WHERE exp_id='id_exploracao1'), 'cadastro2', now(), now(), now(), 'estado2', 1.1, 2.2, 3.3, 4.4);
