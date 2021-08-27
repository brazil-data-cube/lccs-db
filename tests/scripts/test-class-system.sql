SET client_encoding = 'UTF8';

INSERT INTO lccs.classification_systems (created_at, updated_at, id,  authority_name, name, title_translations, description_translations, version)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 6, 'TEST', 'prodes-t', 'pt-br => "PRODES-TESTE", en => "PRODES-TEST"' ,
                                            'pt-br => "Sistema de classificação teste", en => "Test Classification System"', '2.0');


-- CLASSES PRODES-TEST
INSERT INTO lccs.classes (created_at, updated_at, code, name, title_translations, description_translations, classification_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'TEST-DESFLORESTAMENTO', 'test-desflorestamento', 'pt-br => "TESTE-Desflorestamento", en => "TEST-Deforestation"', '', 6),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'TEST-FLORESTA', 'test-floresta', 'pt-br => "TESTE-Floresta" ,en => "TEST-Forest"', '', 6),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'TEST-HIDROGRAFIA', 'test-hidrografia', 'pt-br => "TESTE-Hidrografia", en => "TEST-Hydrography"', '', 6);



