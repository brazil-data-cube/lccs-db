SET client_encoding = 'UTF8';

INSERT INTO lccs.class_systems (created_at, updated_at, id, authority_name, name, description, version)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1, 'INPE', 'Prodes', 'Sistema de Classificação Anual de Desmatamento', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 2, 'INPE', 'Deter-A', 'Sistema de Alertas Diarios de Desmatamento', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 3, 'INPE', 'Deter-B', 'Sistema de Alertas Diarios de Desmatamento', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 4, 'INPE', 'TerraClass', 'Mapa do Uso e Cobertura da Terra', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 5, 'MapBiomas', 'MapBiomas Collection', 'Mapa do Uso e Cobertura da Terra', '3.1'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 6, 'MapBiomas', 'MapBiomas Collection', 'Mapa do Uso e Cobertura da Terra', '4.0');

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,1,'DESFLORESTAMENTO', 'Desflorestamento', '', '#bc0000', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,2,'FLORESTA', 'Floresta', '', '#325a00', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,3,'HIDROGRAFIA', 'Hidrografia', '', '#0000ff', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,4,'NAO_FLORESTA', 'Não Floresta', '', '#aa00ff', 1),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,5,'NUVEM', 'Nuvem', '', '#00ffff', 1),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,6,'RESIDUO', 'Resíduo', '', '#d3ec95', 1);

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 7, 'ALERTA', 'Alerta', '', '#bc0000', 2);

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,8,'CICATRIZ_DE_QUEIMADA', 'Cicatriz de Queimada', '', '#d7191c', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,9,'CS_DESORDENADO', 'x', '', '#fdae61', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,10,'CS_GEOMETRICO', 'y', '', '#fed690', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,11,'DEGRADACAO', 'Degradação', '', '#ffffbf', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,12,'DESMATAMENTO_CR', 'z', '', '#d5eeb1', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,13,'DESMATAMENTO_VEG', 'w', '', '#abdda4', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,14,'MINERACAO', 'Mineração', '', '#6bb0af', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,15,'CORTE_SELETIVO', 'Corte Seletivo', '','#ea633e', 3);

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,16,'AGRICULTURA_ANUAL','Agricultura Anual','Áreas extensas com predomínio de culturas de ciclo anual, sobretudo de grão, com emprego de padrões tecnológicos elevados, tais como uso de sementes certificadas, insumos, defensivos e mecanização, entre outros', '#fff92f', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,17,'AREA_NAO_OBSERVADA','Área Não Observada', 'Areas that could not be interpreted by the presence of clouds at the moment of transit to acquire satellite images, in addition to the recently burned areas',
        '#ffffff', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,18,'AREA_SEM_INFORMACAO','Área sem Informação', '', '#b6b6b6',4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,19,'AREA_URBANA','Área Urbana', 'Manchas urbanas decorrentes da concentração populacional formadora de lugarejos, vilas ou cidades que apresentam infraestrutura diferenciada da área rural apresentando adensamento de arruamentos, casas, prédios e outros equipamentos públicos',
        '#fecfc3', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,20,'DESFLORESTAMENTO','Desflorestamento', '', '#dd1923', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,21,'FLORESTA','Floresta', '',
        '#31643b', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,22,'HIDROGRAFIA','Hidrografia', '', '#394ed2', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,23,'MINERACAO', 'Mineração', 'Áreas de extração mineral com a presença de clareiras e solos expostos, envolvendo desflorestamentos nas proximidades de águas superficiais.',
        '#c4c2bd', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,24,'MOSAICO_DE_OCUPACOES','Mosaico de Ocupações', ' Áreas representadas por uma associação de diversas modalidades de uso da terra e que devido à resolução espacial das imagens de satélite não é possível uma discriminação entre seus componentes. Nesta classe, a agricultura familiar é realizada de forma conjugada ao subsistema de pastagens para criação tradicional de gado.',
        '#ffffbf', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,25,'NAO_FLORESTA','Não Floresta', '',
        '#fa53a7', 4),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,26,'OUTROS', 'Outros', 'São áreas que não se enquadram nas chaves de classificação e apresentavam um padrão de cobertura diferenciada de todas as classes do projeto, tais como afloramentos rochosos, praias fluviais, bancos de areia entre outros.',
        '#631cb4', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,27,'PASTO_COM_SOLO_EXPOSTO','Pasto com Solo Exposto', 'Áreas que após o corte raso da floresta e o desenvolvimento de alguma atividade agropastoril, apresentam uma cobertura de pelo menos 50% de solo exposto', '#8a8c00', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,28,'PASTO_LIMPO','Pasto Limpo', 'Áreas de pastagem em processo produtivo com predomínio de vegetação herbácea, e cobertura de espécies de gramíneas entre 90% e 100%.',
         '#b0b246', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 29,'PASTO_SUJO','Pasto Sujo', 'Áreas de pastagem em processo produtivo com predomínio de vegetação herbácea e cobertura de espécies de gramíneas entre 50% e 80%, associado à presença de vegetação arbustiva esparsa com cobertura entre 20% e 50%.',
        '#eea7cb', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 30,'REFLORESTAMENTO','Reflorestamento', 'Áreas que após o corte raso foram reflorestadas com espécies exóticas com a finalidade comercial.',
         '#2be4ad', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 31,'REGENERACAO_COM_PASTO', 'Regeneração com Pasto',
        'Áreas que, após o corte raso de vegetação natural e o desenvolvimento de alguma atividade agropastoril, encontram-se no início do processo de regeneração da vegetação nativa, apresentando dominância de espécies arbustivas e pioneiras arbóreas. Áreas caracterizadas pela alta diversidade de espécies vegetais.', '#ffa425', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 32,'VEGETACAO_SECUNDARIA', 'Vegetação Secundária',
        'Áreas que, após a supressão total da vegetação florestal, encontram-se em processo avançado de regeneração da vegetação arbustiva e/ou da arbórea ou que foram utilizadas para a prática da silvicultura ou agricultura permanente com uso de espécies nativas ou exóticas.', '#71ff92', 4);

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,33, 'FLORESTA', 'Floresta', '', '#129912', 5),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,34, 'FORMAÇÃO NATURAL NÃO FLORESTAL', 'Formação Natural não Florestal', '', '#bbfcac', 5),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,35, 'AGROPECUÁRIA', 'Agropecuária', '', '#ffffb2', 5),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,36, 'ÁREA NÃO VEGETADA', 'Área não Vegetada', '', '#ea9999 ', 5),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,37, 'CORPO D ÁGUA', 'Corpo D água', '', '#0000ff', 5),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,38, 'NÃO OBSERVADO', 'Não observado', '', '#d5d5e5', 5);

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 39,'FLORESTA NATURAL', 'Floresta Natural', '', '#1f4423', 5, 33),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 40,'FLORESTA PLANTADA', 'Floresta Plantada', '', '#935132', 5, 33);

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 41,'ÁREA UMIDA NATURAL NÃO FLORESTAL', 'Área Úmida Natural não Florestal', '', '#45c2a5', 5, 34),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 42,'FORMAÇÃO CAMPESTRE', 'Formação Campestre', '', '#b8af4f', 5, 34),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 43,'OUTRA FORMAÇÃO NÃO FLORESTAL', 'Outra Formação não Florestal', '', '#bdb76b', 5, 34),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 44,'APICUM', 'Apicum', '', '#968c465', 5, 34);

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 45,'PASTAGEM', 'Pastagem', '', '#ffd966', 5, 35),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 46,'AGRICULTURA', 'Agricultura', '', '#e974ed', 5, 35),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 47,'MOSAICO DE AGRICULTURA OU PASTAGEM', 'Mosaico de Agricultura ou Pastagem', '', '#ffefc3', 5, 35);

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 48,'PRAIA E DUNA', 'Praia e Duna', '', '#dd7e6b', 5, 36),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 49,'INFRAESTRUTURA URBANA', 'Infraestrutura Urbana', '', '#af2a2', 5, 36),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 50,'OUTRA ÁREA NÃO VEGETADA', 'Outra área não Vegetada', '', '#ff99ff', 5, 36),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 51,'AFLORAMENTO ROCHOSO', 'Afloramento Rochoso', '', '#ff8c00', 5, 36),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 52,'MINERAÇÃO', 'Mineração', '', '#8a2be2', 5, 36);

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 53,'AQUICULTURA', 'Aquicultura', '', '#29eee4', 5, 37),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 54,'RIO, LAGO E OCEANO', 'Rio, Lago e Oceano', '', '#0000ff', 5, 37);

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 55,'FORMAÇÃO FLORESTAL', 'Formação Florestal', '', '#006400', 5, 39),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 56,'FORMAÇÃO SAVÂNICA', 'Formação Savânica', '', '#32cd32', 5, 39),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 57,'MANGUE', 'Mangue', '', '#687537', 5, 39);

INSERT INTO lccs.classes (created_at, updated_at, id, code, name, description, style, class_system_id, parent_id)
VALUES  (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 58,'CULTIVO ANUAL E PERENE', 'Cultivo Anual e Perene', '', '#d5a6bd', 5, 46),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 59,'CULTIVO SEMI-PERENE', 'Cultivo Semi-Perene', '', '#c27ba0', 5, 46);