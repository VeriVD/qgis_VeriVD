<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" simplifyLocal="1" styleCategories="AllStyleCategories" simplifyMaxScale="1" simplifyDrawingHints="0" maxScale="0" simplifyAlgorithm="0" labelsEnabled="0" simplifyDrawingTol="1" version="3.10.5-A Coruña" hasScaleBasedVisibilityFlag="0" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" enableorderby="0" type="singleSymbol" forceraster="0">
    <symbols>
      <symbol alpha="1" name="0" clip_to_extent="1" force_rhr="0" type="marker">
        <layer enabled="1" pass="0" class="SimpleMarker" locked="0">
          <prop v="0" k="angle"/>
          <prop v="132,76,56,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="cross2" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="area" k="scale_method"/>
          <prop v="3.5" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
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
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory minScaleDenominator="0" opacity="1" enabled="0" height="15" rotationOffset="270" maxScaleDenominator="1e+08" penColor="#000000" backgroundAlpha="255" sizeType="MM" penAlpha="255" lineSizeType="MM" scaleDependency="Area" backgroundColor="#ffffff" diagramOrientation="Up" barWidth="5" lineSizeScale="3x:0,0,0,0,0,0" scaleBasedVisibility="0" penWidth="0" sizeScale="3x:0,0,0,0,0,0" minimumSize="0" labelPlacementMethod="XHeight" width="15">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" placement="0" dist="0" linePlacementFlags="18" showAll="1" priority="0" zIndex="0">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
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
    <field name="tolerance">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="coord_e">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="coord_n">
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
    <alias field="tolerance" index="1" name=""/>
    <alias field="coord_e" index="2" name=""/>
    <alias field="coord_n" index="3" name=""/>
    <alias field="observation" index="4" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" field="OGC_FID" expression=""/>
    <default applyOnUpdate="0" field="tolerance" expression=""/>
    <default applyOnUpdate="0" field="coord_e" expression=""/>
    <default applyOnUpdate="0" field="coord_n" expression=""/>
    <default applyOnUpdate="0" field="observation" expression=""/>
  </defaults>
  <constraints>
    <constraint constraints="3" notnull_strength="1" unique_strength="1" exp_strength="0" field="OGC_FID"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="tolerance"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="coord_e"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="coord_n"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="observation"/>
  </constraints>
  <constraintExpressions>
    <constraint field="OGC_FID" exp="" desc=""/>
    <constraint field="tolerance" exp="" desc=""/>
    <constraint field="coord_e" exp="" desc=""/>
    <constraint field="coord_n" exp="" desc=""/>
    <constraint field="observation" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="">
    <columns>
      <column name="OGC_FID" width="-1" hidden="0" type="field"/>
      <column name="tolerance" width="-1" hidden="0" type="field"/>
      <column name="coord_e" width="-1" hidden="0" type="field"/>
      <column name="coord_n" width="-1" hidden="0" type="field"/>
      <column name="observation" width="-1" hidden="0" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1">.</editform>
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
    <field editable="1" name="coord_e"/>
    <field editable="1" name="coord_n"/>
    <field editable="1" name="observation"/>
    <field editable="1" name="tolerance"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="OGC_FID"/>
    <field labelOnTop="0" name="coord_e"/>
    <field labelOnTop="0" name="coord_n"/>
    <field labelOnTop="0" name="observation"/>
    <field labelOnTop="0" name="tolerance"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
