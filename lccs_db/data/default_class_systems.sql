SET client_encoding = 'UTF8';

INSERT INTO lccs.class_systems (created_at, updated_at, authority_name, name, description, version)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'Prodes', 'Sistema de Classificação Anual de Desmatamento', '1.0');

-- OBS: CUIDADE COM O class_system_id!
INSERT INTO lccs.classes (created_at, updated_at, code, name, description, class_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESFLORESTAMENTO', 'Desflorestamento', '', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'FLORESTA', 'Floresta', '', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'HIDROGRAFIA', 'Hidrografia', '', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'NAO_FLORESTA', 'Não Floresta', '', 1),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'NUVEM', 'Nuvem', '', 1),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'RESIDUO', 'Resíduo', '', 1);

INSERT INTO lccs.style_formats (created_at, updated_at, name)
VALUES (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'QGIS');