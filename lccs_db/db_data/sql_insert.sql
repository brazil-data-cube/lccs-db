--
-- This file is part of Land Cover Classification System Database Model.
-- Copyright (C) 2019 INPE.
--
-- Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
-- under the terms of the MIT License; see LICENSE file for more details.
--

--Python Land Cover Classification System Database Model insert data.--


-- INSERIR OS DADOS DOS SISTEMAS DE CLASSIFICACAO

INSERT INTO bdc.luc_classification_system (created_at, updated_at, authority_name, system_name, description, version)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'Prodes', 'Annual Deforestation Classification System', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'Deter-A', 'Sistema de Alertas Diarios de Desmatamento', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'Deter-B', 'Sistema de Alertas Diarios de Desmatamento', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'TerraClass', 'Mapa do Uso e Cobertura da Terra', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'MapBiomas', 'MapBiomas Collection', 'Mapa do Uso e Cobertura da Terra', '3.1'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'MapBiomas', 'MapBiomas Collection', 'Mapa do Uso e Cobertura da Terra', '4.0');


-- INSERIR OS DADOS DE CLASSE DO PRODES (atencao no id do sistema de classificacao)

INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESFLORESTAMENTO', 'Desflorestamento', '', '#bc0000', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'FLORESTA', 'Floresta', '', '#325a00', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'HIDROGRAFIA', 'Hidrografia', '', '#0000ff', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'NAO_FLORESTA', 'Não Floresta', '', '#aa00ff', 1),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'NUVEM', 'Nuvem', '', '#00ffff', 1),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'RESIDUO', 'Resíduo', '', '#d3ec95', 1);

-- INSERIR OS DADOS DE CLASSE DO DETER-A

INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ALERTA', 'Alerta', '', '#bc0000', 2);

-- INSERIR OS DADOS DE CLASSE DO DETER-B

INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CICATRIZ_DE_QUEIMADA', 'Cicatriz de Queimada', '', '#d7191c', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CS_DESORDENADO', 'x', '', '#fdae61', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CS_GEOMETRICO', 'y', '', '#fed690', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DEGRADACAO', 'Degradação', '', '#ffffbf', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESMATAMENTO_CR', 'z', '', '#d5eeb1', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESMATAMENTO_VEG', 'w', '', '#abdda4', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'MINERACAO', 'Mineração', '', '#6bb0af', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CORTE_SELETIVO', 'Corte Seletivo', '','#ea633e', 3);

-- INSERIR OS DADOS DE CLASSE DO TERRACLASS

INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'AGRICULTURA_ANUAL','Agricultura Anual','Áreas extensas com predomínio de culturas de ciclo anual, sobretudo de grão, com emprego de padrões tecnológicos elevados, tais como uso de sementes certificadas, insumos, defensivos e mecanização, entre outros', '#fff92f', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'AREA_NAO_OBSERVADA','Área Não Observada', 'Areas that could not be interpreted by the presence of clouds at the moment of transit to acquire satellite images, in addition to the recently burned areas',
        '#ffffff', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'AREA_SEM_INFORMACAO','Área sem Informação', '', '#b6b6b6',4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'AREA_URBANA','Área Urbana', 'Manchas urbanas decorrentes da concentração populacional formadora de lugarejos, vilas ou cidades que apresentam infraestrutura diferenciada da área rural apresentando adensamento de arruamentos, casas, prédios e outros equipamentos públicos',
        '#fecfc3', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESFLORESTAMENTO','Desflorestamento', '', '#dd1923', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'FLORESTA','Floresta', '',
        '#31643b', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'HIDROGRAFIA','Hidrografia', '', '#394ed2', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'MINERACAO', 'Mineração', 'Áreas de extração mineral com a presença de clareiras e solos expostos, envolvendo desflorestamentos nas proximidades de águas superficiais.',
        '#c4c2bd', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'MOSAICO_DE_OCUPACOES','Mosaico de Ocupações', ' Áreas representadas por uma associação de diversas modalidades de uso da terra e que devido à resolução espacial das imagens de satélite não é possível uma discriminação entre seus componentes. Nesta classe, a agricultura familiar é realizada de forma conjugada ao subsistema de pastagens para criação tradicional de gado.',
        '#ffffbf', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'NAO_FLORESTA','Não Floresta', '',
        '#fa53a7', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'OUTROS', 'Outros', 'São áreas que não se enquadram nas chaves de classificação e apresentavam um padrão de cobertura diferenciada de todas as classes do projeto, tais como afloramentos rochosos, praias fluviais, bancos de areia entre outros.',
        '#631cb4', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'PASTO_COM_SOLO_EXPOSTO','Pasto com Solo Exposto', 'Áreas que após o corte raso da floresta e o desenvolvimento de alguma atividade agropastoril, apresentam uma cobertura de pelo menos 50% de solo exposto', '#8a8c00', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'PASTO_LIMPO','Pasto Limpo', 'Áreas de pastagem em processo produtivo com predomínio de vegetação herbácea, e cobertura de espécies de gramíneas entre 90% e 100%.',
         '#b0b246', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'PASTO_SUJO','Pasto Sujo', 'Áreas de pastagem em processo produtivo com predomínio de vegetação herbácea e cobertura de espécies de gramíneas entre 50% e 80%, associado à presença de vegetação arbustiva esparsa com cobertura entre 20% e 50%.',
        '#eea7cb', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'REFLORESTAMENTO','Reflorestamento', 'Áreas que após o corte raso foram reflorestadas com espécies exóticas com a finalidade comercial.',
         '#2be4ad', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'REGENERACAO_COM_PASTO', 'Regeneração com Pasto',
        'Áreas que, após o corte raso de vegetação natural e o desenvolvimento de alguma atividade agropastoril, encontram-se no início do processo de regeneração da vegetação nativa, apresentando dominância de espécies arbustivas e pioneiras arbóreas. Áreas caracterizadas pela alta diversidade de espécies vegetais.', '#ffa425', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'VEGETACAO_SECUNDARIA', 'Vegetação Secundária',
        'Áreas que, após a supressão total da vegetação florestal, encontram-se em processo avançado de regeneração da vegetação arbustiva e/ou da arbórea ou que foram utilizadas para a prática da silvicultura ou agricultura permanente com uso de espécies nativas ou exóticas.', '#71ff92', 4);

    -- INSERIR OS DADOS DE CLASSE DO MapBiomas

INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'FLORESTA', 'Floresta', '', '#129912', 5),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'FORMAÇÃO NATURAL NÃO FLORESTAL', 'Formação Natural não Florestal', '', '#bbfcac', 5),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'AGROPECUÁRIA', 'Agropecuária', '', '#ffffb2', 5),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ÁREA NÃO VEGETADA', 'Área não Vegetada', '', '#ea9999 ', 5),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'CORPO D ÁGUA', 'Corpo D água', '', '#0000ff', 5),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'NÃO OBSERVADO', 'Não observado', '', '#d5d5e5', 5);

INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'FLORESTA NATURAL', 'Floresta Natural', '', '#1f4423', 5, 33),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'FLORESTA PLANTADA', 'Floresta Plantada', '', '#935132', 5, 33);


INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ÁREA UMIDA NATURAL NÃO FLORESTAL', 'Área Úmida Natural não Florestal', '', '#45c2a5', 5, 34),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'FORMAÇÃO CAMPESTRE', 'Formação Campestre', '', '#b8af4f', 5, 34),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'OUTRA FORMAÇÃO NÃO FLORESTAL', 'Outra Formação não Florestal', '', '#bdb76b', 5, 34),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'APICUM', 'Apicum', '', '#968c465', 5, 34);

INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'PASTAGEM', 'Pastagem', '', '#ffd966', 5, 35),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'AGRICULTURA', 'Agricultura', '', '#e974ed', 5, 35),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'MOSAICO DE AGRICULTURA OU PASTAGEM', 'Mosaico de Agricultura ou Pastagem', '', '#ffefc3', 5, 35);

INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'PRAIA E DUNA', 'Praia e Duna', '', '#dd7e6b', 5, 36),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INFRAESTRUTURA URBANA', 'Infraestrutura Urbana', '', '#af2a2', 5, 36),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'OUTRA ÁREA NÃO VEGETADA', 'Outra área não Vegetada', '', '#ff99ff', 5, 36),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'AFLORAMENTO ROCHOSO', 'Afloramento Rochoso', '', '#ff8c00', 5, 36),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'MINERAÇÃO', 'Mineração', '', '#8a2be2', 5, 36);

INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'AQUICULTURA', 'Aquicultura', '', '#29eee4', 5, 37),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'RIO, LAGO E OCEANO', 'Rio, Lago e Oceano', '', '#0000ff', 5, 37);

INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'FORMAÇÃO FLORESTAL', 'Formação Florestal', '', '#006400', 5, 39),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'FORMAÇÃO SAVÂNICA', 'Formação Savânica', '', '#32cd32', 5, 39),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'MANGUE', 'Mangue', '', '#687537', 5, 39);

INSERT INTO bdc.luc_class (created_at, updated_at, codigo, name, description, style, luc_classification_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'CULTIVO ANUAL E PERENE', 'Cultivo Anual e Perene', '', '#d5a6bd', 5, 46),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'CULTIVO SEMI-PERENE', 'Cultivo Semi-Perene', '', '#c27ba0', 5, 46);