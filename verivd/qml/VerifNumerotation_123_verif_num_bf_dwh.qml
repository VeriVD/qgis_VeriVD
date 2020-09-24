<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingHints="1" simplifyDrawingTol="1" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" simplifyLocal="1" readOnly="0" simplifyAlgorithm="0" maxScale="0" version="3.8.2-Zanzibar" labelsEnabled="0" simplifyMaxScale="1" minScale="1e+08">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="singleSymbol" forceraster="0" enableorderby="0" symbollevels="0">
    <symbols>
      <symbol name="0" force_rhr="0" clip_to_extent="1" type="fill" alpha="0.1">
        <layer class="SimpleLine" enabled="1" pass="0" locked="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0,0,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory minScaleDenominator="0" scaleDependency="Area" backgroundAlpha="255" backgroundColor="#ffffff" sizeScale="3x:0,0,0,0,0,0" lineSizeType="MM" maxScaleDenominator="1e+08" height="15" labelPlacementMethod="XHeight" minimumSize="0" barWidth="5" rotationOffset="270" enabled="0" penAlpha="255" penColor="#000000" width="15" scaleBasedVisibility="0" diagramOrientation="Up" opacity="1" penWidth="0" sizeType="MM" lineSizeScale="3x:0,0,0,0,0,0">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute color="#000000" label="" field=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings linePlacementFlags="18" dist="0" placement="1" obstacle="0" showAll="1" priority="0" zIndex="0">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="OGC_FID">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="identdn">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="numero">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="egris_egrid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="validite_txt">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="integralite_txt">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="genre_txt">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="superficie_totale">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="superficie">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="superficierf">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="observation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" index="0" field="OGC_FID"/>
    <alias name="" index="1" field="identdn"/>
    <alias name="" index="2" field="numero"/>
    <alias name="" index="3" field="egris_egrid"/>
    <alias name="" index="4" field="validite_txt"/>
    <alias name="" index="5" field="integralite_txt"/>
    <alias name="" index="6" field="genre_txt"/>
    <alias name="" index="7" field="superficie_totale"/>
    <alias name="" index="8" field="superficie"/>
    <alias name="" index="9" field="superficierf"/>
    <alias name="" index="10" field="observation"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" applyOnUpdate="0" field="OGC_FID"/>
    <default expression="" applyOnUpdate="0" field="identdn"/>
    <default expression="" applyOnUpdate="0" field="numero"/>
    <default expression="" applyOnUpdate="0" field="egris_egrid"/>
    <default expression="" applyOnUpdate="0" field="validite_txt"/>
    <default expression="" applyOnUpdate="0" field="integralite_txt"/>
    <default expression="" applyOnUpdate="0" field="genre_txt"/>
    <default expression="" applyOnUpdate="0" field="superficie_totale"/>
    <default expression="" applyOnUpdate="0" field="superficie"/>
    <default expression="" applyOnUpdate="0" field="superficierf"/>
    <default expression="" applyOnUpdate="0" field="observation"/>
  </defaults>
  <constraints>
    <constraint notnull_strength="1" constraints="3" unique_strength="1" field="OGC_FID" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" field="identdn" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" field="numero" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" field="egris_egrid" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" field="validite_txt" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" field="integralite_txt" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" field="genre_txt" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" field="superficie_totale" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" field="superficie" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" field="superficierf" exp_strength="0"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" field="observation" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="OGC_FID"/>
    <constraint exp="" desc="" field="identdn"/>
    <constraint exp="" desc="" field="numero"/>
    <constraint exp="" desc="" field="egris_egrid"/>
    <constraint exp="" desc="" field="validite_txt"/>
    <constraint exp="" desc="" field="integralite_txt"/>
    <constraint exp="" desc="" field="genre_txt"/>
    <constraint exp="" desc="" field="superficie_totale"/>
    <constraint exp="" desc="" field="superficie"/>
    <constraint exp="" desc="" field="superficierf"/>
    <constraint exp="" desc="" field="observation"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column name="OGC_FID" type="field" hidden="0" width="-1"/>
      <column name="identdn" type="field" hidden="0" width="-1"/>
      <column name="numero" type="field" hidden="0" width="-1"/>
      <column name="egris_egrid" type="field" hidden="0" width="-1"/>
      <column name="validite_txt" type="field" hidden="0" width="-1"/>
      <column name="integralite_txt" type="field" hidden="0" width="-1"/>
      <column name="genre_txt" type="field" hidden="0" width="-1"/>
      <column name="superficie_totale" type="field" hidden="0" width="-1"/>
      <column name="superficie" type="field" hidden="0" width="-1"/>
      <column name="superficierf" type="field" hidden="0" width="-1"/>
      <column name="observation" type="field" hidden="0" width="-1"/>
      <column type="actions" hidden="1" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Les formulaires QGIS peuvent avoir une fonction Python qui sera appelée à l'ouverture du formulaire.

Utilisez cette fonction pour ajouter plus de fonctionnalités à vos formulaires.

Entrez le nom de la fonction dans le champ "Fonction d'initialisation Python".
Voici un exemple à suivre:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
    geom = feature.geometry()
    control = dialog.findChild(QWidget, "MyLineEdit")

]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="OGC_FID" editable="1"/>
    <field name="egris_egrid" editable="1"/>
    <field name="genre_txt" editable="1"/>
    <field name="identdn" editable="1"/>
    <field name="integralite_txt" editable="1"/>
    <field name="numero" editable="1"/>
    <field name="observation" editable="1"/>
    <field name="superficie" editable="1"/>
    <field name="superficie_totale" editable="1"/>
    <field name="superficierf" editable="1"/>
    <field name="validite_txt" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="OGC_FID" labelOnTop="0"/>
    <field name="egris_egrid" labelOnTop="0"/>
    <field name="genre_txt" labelOnTop="0"/>
    <field name="identdn" labelOnTop="0"/>
    <field name="integralite_txt" labelOnTop="0"/>
    <field name="numero" labelOnTop="0"/>
    <field name="observation" labelOnTop="0"/>
    <field name="superficie" labelOnTop="0"/>
    <field name="superficie_totale" labelOnTop="0"/>
    <field name="superficierf" labelOnTop="0"/>
    <field name="validite_txt" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
