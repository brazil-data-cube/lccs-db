SET client_encoding = 'UTF8';

INSERT INTO lccs.class_systems (created_at, updated_at, id, authority_name, name, description, version)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 6, 'TEST', 'PRODES-TEST', 'Sistema de Classificação de Teste', '2.0');


-- CLASSES PRODES-TEST
INSERT INTO lccs.classes (created_at, updated_at, code, name, description, class_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'TEST-DESFLORESTAMENTO', 'TEST-Desflorestamento', '', 6 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'TEST-FLORESTA', 'Floresta', '', 6 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'TEST-HIDROGRAFIA', 'Hidrografia', '', 6 );


