SET client_encoding = 'UTF8';

INSERT INTO lccs.classification_systems (created_at, updated_at, authority_name, name, description, version)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'PRODES', 'Sistema de Classificação Anual de Desmatamento', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'PRODES-SubClasses', 'Sistema de Classificação Anual de Desmatamento', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'TerraClass-AMZ', 'Projeto TerraClass Mapeamento do Uso e Cobertura da Terra', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'TerraClass-SubClass_AMZ', 'Sub classes do Projeto TerraClass', '1.0'),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'INPE', 'DETER-B-AMZ', 'Sistema de Alertas Diarios de Desmatamento', '1.0');


-- CLASSES PRODES
INSERT INTO lccs.classes (created_at, updated_at, code, name, description, classification_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESFLORESTAMENTO', 'Desflorestamento', '', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'FLORESTA', 'Floresta', '', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'HIDROGRAFIA', 'Hidrografia', '', 1 ),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'NAO_FLORESTA', 'Não Floresta', '', 1),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'NUVEM', 'Nuvem', '', 1),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'RESIDUO', 'Resíduo', '', 1);

-- SUBCLASSES PRODES
INSERT INTO lccs.classes (created_at, updated_at, code, name, description, classification_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'd2007','Desflorestamento 2007','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'd2008','Desflorestamento 2008','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'd2009','Desflorestamento 2009','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'd2010','Desflorestamento 2010','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'd2011','Desflorestamento 2011','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'd2012','Desflorestamento 2012','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'd2013','Desflorestamento 2013','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'd2014','Desflorestamento 2014','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'd2015','Desflorestamento 2015','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'd2016','Desflorestamento 2016','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'd2017','Desflorexitestamento 2017','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'FLORESTA','Floresta','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'HIDROGRAFIA','Hidrografia','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'NAO_FLORESTA','Não Floresta     ','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'NAO_FLORESTA2','Não Floresta 2   ','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'NUVEM','Nuvem','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'r2010','Resíduo 2010','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'r2011','Resíduo 2011','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'r2012','Resíduo 2012','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'r2013','Resíduo 2013','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'r2014','Resíduo 2014','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'r2015','Resíduo 2015','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'r2016','Resíduo 2016','',2),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'r2017','Resíduo 2017','',2);

-- CLASSES TERRACLASS-AMZ
INSERT INTO lccs.classes (created_at, updated_at, code, name, description, classification_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'AGRICULTURA_ANUAL','Agricultura Anual','Áreas extensas com predomínio de culturas de ciclo anual, sobretudo de grão, com emprego de padrões tecnológicos elevados, tais como uso de sementes certificadas, insumos, defensivos e mecanização, entre outros', 3),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'AREA_NAO_OBSERVADA','Área Não Observada', 'Areas that could not be interpreted by the presence of clouds at the moment of transit to acquire satellite images, in addition to the recently burned areas', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'AREA_SEM_INFORMACAO','Área sem Informação', '', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'AREA_URBANA','Área Urbana', 'Manchas urbanas decorrentes da concentração populacional formadora de lugarejos, vilas ou cidades que apresentam infraestrutura diferenciada da área rural apresentando adensamento de arruamentos, casas, prédios e outros equipamentos públicos', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESFLORESTAMENTO','Desflorestamento', '', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'FLORESTA','Floresta', '', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'HIDROGRAFIA','Hidrografia', '', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'MINERACAO', 'Mineração', 'Áreas de extração mineral com a presença de clareiras e solos expostos, envolvendo desflorestamentos nas proximidades de águas superficiais.', 3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'MOSAICO_DE_OCUPACOES','Mosaico de Ocupações', ' Áreas representadas por uma associação de diversas modalidades de uso da terra e que devido à resolução espacial das imagens de satélite não é possível uma discriminação entre seus componentes. Nesta classe, a agricultura familiar é realizada de forma conjugada ao subsistema de pastagens para criação tradicional de gado.', 3),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'NAO_FLORESTA','Não Floresta', '',3),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'OUTROS', 'Outros', 'São áreas que não se enquadram nas chaves de classificação e apresentavam um padrão de cobertura diferenciada de todas as classes do projeto, tais como afloramentos rochosos, praias fluviais, bancos de areia entre outros.', 3),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'PASTO_COM_SOLO_EXPOSTO','Pasto com Solo Exposto', 'Áreas que após o corte raso da floresta e o desenvolvimento de alguma atividade agropastoril, apresentam uma cobertura de pelo menos 50% de solo exposto', 3),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'PASTO_LIMPO','Pasto Limpo', 'Áreas de pastagem em processo produtivo com predomínio de vegetação herbácea, e cobertura de espécies de gramíneas entre 90% e 100%.', 3),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'PASTO_SUJO','Pasto Sujo', 'Áreas de pastagem em processo produtivo com predomínio de vegetação herbácea e cobertura de espécies de gramíneas entre 50% e 80%, associado à presença de vegetação arbustiva esparsa com cobertura entre 20% e 50%.',3),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'REFLORESTAMENTO','Reflorestamento', 'Áreas que após o corte raso foram reflorestadas com espécies exóticas com a finalidade comercial.', 3),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'REGENERACAO_COM_PASTO', 'Regeneração com Pasto',
        'Áreas que, após o corte raso de vegetação natural e o desenvolvimento de alguma atividade agropastoril, encontram-se no início do processo de regeneração da vegetação nativa, apresentando dominância de espécies arbustivas e pioneiras arbóreas. Áreas caracterizadas pela alta diversidade de espécies vegetais.', 3),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'VEGETACAO_SECUNDARIA', 'Vegetação Secundária',
        'Áreas que, após a supressão total da vegetação florestal, encontram-se em processo avançado de regeneração da vegetação arbustiva e/ou da arbórea ou que foram utilizadas para a prática da silvicultura ou agricultura permanente com uso de espécies nativas ou exóticas.', 3);

-- SUBCLASSES TERRACLASS-AMZ
INSERT INTO lccs.classes (created_at, updated_at, code, name, description, classification_system_id)
VALUES (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'AGRICULTURA_ANUAL','Agricultura Anual',' Áreas extensas com predomínio de culturas de ciclo anual, sobretudo de grão, com emprego de padrões tecnológicos elevados, tais como uso de sementes certificadas, insumos, defensivos e mecanização, entre outros.', 4),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'AREA_NAO_OBSERVADA', 'Área Não Observada', 'Áreas que tiveram sua interpretação impossibilitada pela presença de nuvens, no momento de passage para aquisição das imagens de satélite, além das áreas recentemente queimadas.', 4),
       (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'AREA_URBANA', 'Área Urbana', 'Manchas urbanas decorrentes da concentração populacional formadora de lugarejos, vilas ou cidades que apresentam infra-estrutura diferenciada da área rural apresentando adensamento de arruamentos, casas, prédios e outros equipamentos públicos.', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'DESFLORESTAMENTO', 'Desflorestamento', '', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'DESFLORESTAMENTO_2004', 'Desflorestamento 2004 ', '', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'DESFLORESTAMENTO_2008', 'Desflorestamento 2008', '', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'DESFLORESTAMENTO_2010', 'Desflorestamento 2010', '', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'DESFLORESTAMENTO_2012', 'Desflorestamento 2012', '', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'DESFLORESTAMENTO_2014', 'Desflorestamento 2014', '', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'FLORESTA', 'Floresta', '', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'HIDROGRAFIA', 'Hidrografia', '', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'MINERACAO', 'Mineração', 'Áreas de extração mineral com a presença de clareiras e solos expostos, envolvendo desflorestamentos nas proximidades de águas superficiais.', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'MOSAICO_DE_OCUPACOES', 'Mosaico de Ocupações', 'Áreas representadas por uma associação de diversas modalidades de uso da terra e que devido à resolução espacial das imagens de satélite não é possível uma discriminação entre seus componentes. Nesta classe, a agricultura familiar é realizada de forma conjugada ao subsistema de pastagens para criação tradicional de gado.', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'NAO_FLORESTA', 'Não Floresta', '', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'OUTROS', 'Outros', 'São áreas que não se enquadram nas chaves de classificação e apresentavam um padrão de cobertura diferenciada de todas as classes do projeto, tais como afloramentos rochosos, praias fluviais, bancos de areia entre outros.', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'PASTO_COM_SOLO_EXPOSTO', 'Pasto com Solo Exposto', 'Áreas que após o corte raso da floresta e o desenvolvimento de alguma atividade agropastoril, apresentam uma cobertura de pelo menos 50% de solo exposto.', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'PASTO_LIMPO', 'Pasto Limpo', 'Áreas de pastagem em processo produtivo com predomínio de vegetação herbácea, e cobertura de espécies de gramíneas entre 90% e 100%.', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'PASTO_SUJO', 'PASTO_SUJO', 'Áreas de pastagem em processo produtivo com predomínio de vegetação herbácea e cobertura de espécies de gramíneas entre 50% e 80%, associado à presença de vegetação arbustiva esparsa com cobertura entre 20% e 50%.', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'REFLORESTAMENTO', 'Reflorestamento', 'Áreas que após o corte raso foram reflorestadas com espécies exóticas com a finalidade comercial.', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'REGENERACAO_COM_PASTO', 'Regeneração com Pasto', 'Áreas que, após o corte raso de vegetação natural e o desenvolvimento de alguma atividade agropastoril, encontram-se no início do processo de regeneração da vegetação nativa, apresentando dominância de espécies arbustivas e pioneiras arbóreas. Áreas caracterizadas pela alta diversidade de espécies vegetais.', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,'VEGETACAO_SECUNDARIA', 'Vegetação Secundária', 'Áreas que, após a supressão total da vegetação florestal, encontram-se em processo avançado de regeneração da vegetação arbustiva e/ou da arbórea ou que foram utilizadas para a prática da silvicultura ou agricultura permanente com uso de espécies nativas ou exóticas.', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'AREA_SEM_INFORMACAO_EM_2004', 'Área sem Informação em 2004', '', 4),
        (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'AREA_SEM_INFORMACAO_EM_2008', 'Área sem Informação em 2008', '', 4);

-- CLASSES DETER-B-AMZ
INSERT INTO lccs.classes (created_at, updated_at, code, name, description, classification_system_id)
VALUES  (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CICATRIZ_DE_QUEIMADA', 'Cicatriz de Queimada', '', 5),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CS_DESORDENADO', 'x', '', 5),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CS_GEOMETRICO', 'y', '', 5),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DEGRADACAO', 'Degradação', '', 5),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESMATAMENTO_CR', 'z', '', 5),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'DESMATAMENTO_VEG', 'w', '', 5),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'MINERACAO', 'Mineração', '', 5),
        (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'CORTE_SELETIVO', 'Corte Seletivo', '', 5);

INSERT INTO lccs.style_formats (created_at, updated_at, name)
VALUES (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'QGIS');

INSERT INTO lccs.style_formats (created_at, updated_at, name)
VALUES (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'TerraView');

INSERT INTO lccs.style_formats (created_at, updated_at, name)
VALUES (CURRENT_TIMESTAMP,CURRENT_TIMESTAMP, 'GeoServer');