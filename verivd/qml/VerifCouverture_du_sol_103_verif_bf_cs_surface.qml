<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingTol="1" readOnly="0" simplifyLocal="1" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1" styleCategories="AllStyleCategories" maxScale="0" version="3.4.4-Madeira" labelsEnabled="0" minScale="1e+08" simplifyMaxScale="1" simplifyAlgorithm="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" type="singleSymbol" enableorderby="0" symbollevels="0">
    <symbols>
      <symbol force_rhr="0" alpha="1" clip_to_extent="1" type="fill" name="0">
        <layer pass="0" locked="0" class="SimpleFill" enabled="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="215,255,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1.46" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
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
    <DiagramCategory barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" rotationOffset="270" penWidth="0" scaleBasedVisibility="0" width="15" penColor="#000000" minimumSize="0" sizeScale="3x:0,0,0,0,0,0" diagramOrientation="Up" sizeType="MM" lineSizeScale="3x:0,0,0,0,0,0" minScaleDenominator="0" height="15" enabled="0" labelPlacementMethod="XHeight" lineSizeType="MM" backgroundColor="#ffffff" backgroundAlpha="255" opacity="1" scaleDependency="Area">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" obstacle="0" dist="0" linePlacementFlags="18" zIndex="0" showAll="1" placement="1">
    <properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
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
    <field name="tolerancesurface">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tolerancelargeur">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nomcomparaison">
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
    <alias field="tolerancesurface" index="1" name=""/>
    <alias field="tolerancelargeur" index="2" name=""/>
    <alias field="nomcomparaison" index="3" name=""/>
    <alias field="observation" index="4" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="OGC_FID" applyOnUpdate="0" expression=""/>
    <default field="tolerancesurface" applyOnUpdate="0" expression=""/>
    <default field="tolerancelargeur" applyOnUpdate="0" expression=""/>
    <default field="nomcomparaison" applyOnUpdate="0" expression=""/>
    <default field="observation" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint field="OGC_FID" unique_strength="1" exp_strength="0" constraints="3" notnull_strength="1"/>
    <constraint field="tolerancesurface" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="tolerancelargeur" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="nomcomparaison" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="observation" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="OGC_FID" exp="" desc=""/>
    <constraint field="tolerancesurface" exp="" desc=""/>
    <constraint field="tolerancelargeur" exp="" desc=""/>
    <constraint field="nomcomparaison" exp="" desc=""/>
    <constraint field="observation" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" hidden="0" type="field" name="OGC_FID"/>
      <column width="-1" hidden="0" type="field" name="tolerancesurface"/>
      <column width="-1" hidden="0" type="field" name="tolerancelargeur"/>
      <column width="-1" hidden="0" type="field" name="nomcomparaison"/>
      <column width="-1" hidden="0" type="field" name="observation"/>
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
    <field editable="1" name="nomcomparaison"/>
    <field editable="1" name="observation"/>
    <field editable="1" name="tolerancelargeur"/>
    <field editable="1" name="tolerancesurface"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="OGC_FID"/>
    <field labelOnTop="0" name="nomcomparaison"/>
    <field labelOnTop="0" name="observation"/>
    <field labelOnTop="0" name="tolerancelargeur"/>
    <field labelOnTop="0" name="tolerancesurface"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
