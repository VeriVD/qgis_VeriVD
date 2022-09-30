<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" simplifyMaxScale="1" labelsEnabled="0" version="3.8.2-Zanzibar" simplifyAlgorithm="0" styleCategories="AllStyleCategories" minScale="1e+08" simplifyLocal="1" simplifyDrawingTol="1" readOnly="0" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" forceraster="0" enableorderby="0" type="singleSymbol">
    <symbols>
      <symbol clip_to_extent="1" name="0" force_rhr="0" alpha="1" type="fill">
        <layer class="SimpleFill" locked="0" pass="0" enabled="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,0,0,180" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="204,255,1,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="2" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory sizeType="MM" backgroundAlpha="255" enabled="0" labelPlacementMethod="XHeight" penColor="#000000" minimumSize="0" barWidth="5" rotationOffset="270" lineSizeScale="3x:0,0,0,0,0,0" opacity="1" height="15" scaleDependency="Area" sizeScale="3x:0,0,0,0,0,0" penAlpha="255" minScaleDenominator="0" scaleBasedVisibility="0" lineSizeType="MM" backgroundColor="#ffffff" width="15" maxScaleDenominator="1e+08" penWidth="0" diagramOrientation="Up">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" showAll="1" placement="1" linePlacementFlags="18" zIndex="0" obstacle="0" priority="0">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
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
    <field name="localisation_xtf_id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="genre">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="xtf_id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lieu_denomme_de">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ufid">
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
    <alias field="OGC_FID" index="0" name=""/>
    <alias field="localisation_xtf_id" index="1" name=""/>
    <alias field="genre" index="2" name=""/>
    <alias field="xtf_id" index="3" name=""/>
    <alias field="lieu_denomme_de" index="4" name=""/>
    <alias field="ufid" index="5" name=""/>
    <alias field="observation" index="6" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="OGC_FID" applyOnUpdate="0" expression=""/>
    <default field="localisation_xtf_id" applyOnUpdate="0" expression=""/>
    <default field="genre" applyOnUpdate="0" expression=""/>
    <default field="xtf_id" applyOnUpdate="0" expression=""/>
    <default field="lieu_denomme_de" applyOnUpdate="0" expression=""/>
    <default field="ufid" applyOnUpdate="0" expression=""/>
    <default field="observation" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint field="OGC_FID" constraints="3" notnull_strength="1" unique_strength="1" exp_strength="0"/>
    <constraint field="localisation_xtf_id" constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint field="genre" constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint field="xtf_id" constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint field="lieu_denomme_de" constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint field="ufid" constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint field="observation" constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="OGC_FID" desc="" exp=""/>
    <constraint field="localisation_xtf_id" desc="" exp=""/>
    <constraint field="genre" desc="" exp=""/>
    <constraint field="xtf_id" desc="" exp=""/>
    <constraint field="lieu_denomme_de" desc="" exp=""/>
    <constraint field="ufid" desc="" exp=""/>
    <constraint field="observation" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column name="OGC_FID" width="-1" hidden="0" type="field"/>
      <column name="localisation_xtf_id" width="-1" hidden="0" type="field"/>
      <column name="genre" width="-1" hidden="0" type="field"/>
      <column name="xtf_id" width="-1" hidden="0" type="field"/>
      <column name="lieu_denomme_de" width="-1" hidden="0" type="field"/>
      <column name="ufid" width="-1" hidden="0" type="field"/>
      <column name="observation" width="-1" hidden="0" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
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
    <field editable="1" name="OGC_FID"/>
    <field editable="1" name="genre"/>
    <field editable="1" name="lieu_denomme_de"/>
    <field editable="1" name="localisation_xtf_id"/>
    <field editable="1" name="observation"/>
    <field editable="1" name="ufid"/>
    <field editable="1" name="xtf_id"/>
  </editable>
  <labelOnTop>
    <field name="OGC_FID" labelOnTop="0"/>
    <field name="genre" labelOnTop="0"/>
    <field name="lieu_denomme_de" labelOnTop="0"/>
    <field name="localisation_xtf_id" labelOnTop="0"/>
    <field name="observation" labelOnTop="0"/>
    <field name="ufid" labelOnTop="0"/>
    <field name="xtf_id" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>lieu_denomme_de</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
