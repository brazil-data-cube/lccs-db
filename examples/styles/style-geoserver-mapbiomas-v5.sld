<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
    <sld:NamedLayer>
        <sld:Name>Default Styler</sld:Name>
        <sld:UserStyle>
            <sld:Name>Default Styler</sld:Name>
            <sld:FeatureTypeStyle>
                <sld:Name>Mapbiomas_estilo</sld:Name>
                <sld:Rule>
                 <sld:RasterSymbolizer>
                 <sld:ColorMap type="values">
                        <sld:ColorMapEntry color="#274e13" quantity="3" label="Formação Florestal" opacity="1"/>
                        <sld:ColorMapEntry color="#32cd32" quantity="4" label="Formação Savânica"  opacity="1"/>
                        <sld:ColorMapEntry color="#687537" quantity="5" label="Mangue" opacity="1"/>
                        <sld:ColorMapEntry color="#935132" quantity="9" label="Floresta Plantada" opacity="1"/>
						<sld:ColorMapEntry color="#45c2a5" quantity="11" label="Área Úmida não Florestal" opacity="1"/>
						<sld:ColorMapEntry color="#b8af4f" quantity="12" label="Formação Campestre" opacity="1"/>
						<sld:ColorMapEntry color="#bdb76b" quantity="13" label="Outra Formação Natural não Florestal" opacity="1"/>
						<sld:ColorMapEntry label="Pastagem" color="#ffd966" quantity="15" opacity="1"/>
						<sld:ColorMapEntry label="Agricultura" color="#e974ed" quantity="18" opacity="1"/>
						<sld:ColorMapEntry label="Cultura Anual e Perene" color="#d5a6bd" quantity="19" opacity="1"/>
						<sld:ColorMapEntry label="Cultura Semi-Perene" color="#c27ba0" quantity="20" opacity="1"/>
						<sld:ColorMapEntry label="Mosaico de Agricultura e Pastagem" color="#ffefc3" quantity="21" opacity="1"/>
						<sld:ColorMapEntry label="Praia e Duna" color="#dd7e6b" quantity="23" opacity="1"/>
						<sld:ColorMapEntry label="Infraestrutura Urbana" color="#af2a2a" quantity="24" opacity="1"/>
						<sld:ColorMapEntry label="Outra Área não Vegetada" color="#ff99ff" quantity="25" opacity="1"/>
						<sld:ColorMapEntry label="Náo observado" color="#d5d5e5" quantity="27" opacity="1"/>
						<sld:ColorMapEntry label="Afloramento Rochoso" color="#ff8c00" quantity="29" opacity="1"/>
						<sld:ColorMapEntry label="Mineração" color="#8a2be2" quantity="30" opacity="1"/>
						<sld:ColorMapEntry label="Aquicultura" color="#29eee4" quantity="31" opacity="1"/>
						<sld:ColorMapEntry label="Rio, Lago e Oceano" color="#0000ff" quantity="33" opacity="1"/>
						<sld:ColorMapEntry label="Apicum" color="#968c46" quantity="32" opacity="1"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:NamedLayer>
</sld:StyledLayerDescriptor>
