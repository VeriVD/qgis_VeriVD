<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingTol="1" simplifyMaxScale="1" styleCategories="AllStyleCategories" simplifyLocal="1" minScale="1e+08" version="3.8.2-Zanzibar" hasScaleBasedVisibilityFlag="0" maxScale="0" readOnly="0" labelsEnabled="0" simplifyDrawingHints="1" simplifyAlgorithm="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" forceraster="0" symbollevels="0" type="singleSymbol">
    <symbols>
      <symbol clip_to_extent="1" name="0" type="line" alpha="1" force_rhr="0">
        <layer pass="0" class="SimpleLine" enabled="1" locked="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="245,0,16,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.2" k="line_width"/>
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
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory sizeType="MM" lineSizeType="MM" maxScaleDenominator="1e+08" lineSizeScale="3x:0,0,0,0,0,0" barWidth="5" penColor="#000000" rotationOffset="270" enabled="0" opacity="1" backgroundColor="#ffffff" diagramOrientation="Up" penAlpha="255" backgroundAlpha="255" sizeScale="3x:0,0,0,0,0,0" width="15" minScaleDenominator="0" scaleDependency="Area" labelPlacementMethod="XHeight" minimumSize="0" scaleBasedVisibility="0" height="15" penWidth="0">
      <fontProperties style="" description="MS Shell Dlg 2,5.5,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" zIndex="0" placement="2" dist="0" showAll="1" priority="0" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
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
    <field name="source">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_overlaps">
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
    <alias name="" field="OGC_FID" index="0"/>
    <alias name="" field="source" index="1"/>
    <alias name="" field="_overlaps" index="2"/>
    <alias name="" field="observation" index="3"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="OGC_FID" applyOnUpdate="0" expression=""/>
    <default field="source" applyOnUpdate="0" expression=""/>
    <default field="_overlaps" applyOnUpdate="0" expression=""/>
    <default field="observation" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint constraints="3" notnull_strength="1" field="OGC_FID" unique_strength="1" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="source" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="_overlaps" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="observation" unique_strength="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="OGC_FID" exp=""/>
    <constraint desc="" field="source" exp=""/>
    <constraint desc="" field="_overlaps" exp=""/>
    <constraint desc="" field="observation" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column hidden="0" width="-1" name="OGC_FID" type="field"/>
      <column hidden="0" width="-1" name="source" type="field"/>
      <column hidden="0" width="-1" name="_overlaps" type="field"/>
      <column hidden="0" width="-1" name="observation" type="field"/>
      <column hidden="1" width="-1" type="actions"/>
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
    <field editable="1" name="_overlaps"/>
    <field editable="1" name="observation"/>
    <field editable="1" name="source"/>
  </editable>
  <labelOnTop>
    <field name="OGC_FID" labelOnTop="0"/>
    <field name="_overlaps" labelOnTop="0"/>
    <field name="observation" labelOnTop="0"/>
    <field name="source" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
