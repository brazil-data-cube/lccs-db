SET client_encoding = 'UTF8';

INSERT INTO lccs.classification_systems (created_at, updated_at, authority_name, name, title_translations, description_translations, version)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'prodes', 'pt-br => "PRODES", en => "PRODES"',
        'pt-br => "Sistema de Classificação Anual de Desmatamento", en => "Annual Deforestation Classification System"', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'terraclass-amz', 'pt-br => "TerraClass Amazônia", en => "TerraClass Amazon"',
        'pt-br => "Projeto TerraClass Mapeamento do Uso e Cobertura da Terra", en => "TerraClass Project Land Use and Land Cover Mapping"', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'deter-amz', 'pt-br => "DETER Amazônia", en => "DETER Amazon"',
       'pt-br => "Sistema de Alertas Diários de Desmatamento" , en => "Daily Deforestation Alert System"', '1.0');

INSERT INTO lccs.classes (created_at, updated_at, code, name, title_translations, description_translations, classification_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESFLORESTAMENTO', 'desflorestamento', 'pt-br => "Desflorestamento", en => "Deforestation"', '', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'FLORESTA', 'floresta', 'pt-br => "Floresta" ,en => "Forest"', '', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'HIDROGRAFIA', 'hidrografia', 'pt-br => "Hidrografia", en => "Hydrography"', '', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'NAO_FLORESTA', 'nao-floresta', 'pt-br => "Não Floresta", en => "No Forest"', '', 1),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'NUVEM', 'nuvem', 'pt-br => "Nuvem", en => "Cloud"', '', 1),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'RESIDUO', 'residuo', 'pt-br => "Resíduo", en => "Residue"', '', 1);


INSERT INTO lccs.classes (created_at, updated_at, code, name, title_translations, description_translations, classification_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CICATRIZ_DE_QUEIMADA', 'cicatriz-queimada', 'pt-br => "Cicatriz de Queimada", en => "Burn scar"', '', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CS_DESORDENADO', 'cs-desordenado', 'pt-br => "Corte Seletivo Tipo 1 (Desordenado)", en => "Type 1 Selective Cut (Disordered)"', '', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CS_GEOMETRICO', 'cs-geometrico', 'pt-br => "Corte Seletivo Tipo 2 (Geométrico)", en => "Type 2 Selective Cut (Geometric)"','', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DEGRADACAO', 'degradacao', 'pt-br => "Degradação", en => "Degradation"','', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESMATAMENTO_CR', 'desmatamento-cr', 'pt-br => "Desmatamento Corte Raso", en => "Clear Cut Deforestation"','', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESMATAMENTO_VEG', 'desmatamento-veg', 'pt-br => "Desmatamento com Vegetação", en => "Deforestation with Vegetation"','', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'MINERACAO', 'mineracao', 'pt-br => "Mineração", en => "Mining"', '', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CORTE_SELETIVO', 'corte-seletivo', 'pt-br => "Corte Seletivo", en => "Selective Cut"', '', 3);


INSERT INTO lccs.style_formats (created_at, updated_at, name)
VALUES (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'QML-Feature-Point'),
       (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'QML-Feature-Polygon'),
       (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'SLD-Coverage'),
       (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'SLD-Feature-Point'),
       (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'SLD-Feature-Polygon'),
       (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'SLD-Feature-Line');