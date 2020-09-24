<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" minScale="1e+08" readOnly="0" simplifyAlgorithm="0" simplifyDrawingTol="1" simplifyMaxScale="1" version="3.4.4-Madeira" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="0" labelsEnabled="0" simplifyLocal="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" enableorderby="0" type="singleSymbol" symbollevels="0">
    <symbols>
      <symbol force_rhr="0" clip_to_extent="1" alpha="1" name="0" type="marker">
        <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="5"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="3.75"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
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
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory barWidth="5" backgroundColor="#ffffff" backgroundAlpha="255" sizeType="MM" rotationOffset="270" maxScaleDenominator="1e+08" minScaleDenominator="0" opacity="1" penWidth="0" diagramOrientation="Up" labelPlacementMethod="XHeight" penColor="#000000" minimumSize="0" lineSizeScale="3x:0,0,0,0,0,0" penAlpha="255" scaleBasedVisibility="0" height="15" lineSizeType="MM" sizeScale="3x:0,0,0,0,0,0" enabled="0" scaleDependency="Area" width="15">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="0" zIndex="0" obstacle="0" showAll="1" priority="0" dist="0" linePlacementFlags="18">
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
    <field name="source">
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
    <alias name="" field="OGC_FID" index="0"/>
    <alias name="" field="source" index="1"/>
    <alias name="" field="genre" index="2"/>
    <alias name="" field="coord_e" index="3"/>
    <alias name="" field="coord_n" index="4"/>
    <alias name="" field="observation" index="5"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="OGC_FID" applyOnUpdate="0" expression=""/>
    <default field="source" applyOnUpdate="0" expression=""/>
    <default field="genre" applyOnUpdate="0" expression=""/>
    <default field="coord_e" applyOnUpdate="0" expression=""/>
    <default field="coord_n" applyOnUpdate="0" expression=""/>
    <default field="observation" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" notnull_strength="1" exp_strength="0" field="OGC_FID" constraints="3"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" field="source" constraints="0"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" field="genre" constraints="0"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" field="coord_e" constraints="0"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" field="coord_n" constraints="0"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" field="observation" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="OGC_FID" exp="" desc=""/>
    <constraint field="source" exp="" desc=""/>
    <constraint field="genre" exp="" desc=""/>
    <constraint field="coord_e" exp="" desc=""/>
    <constraint field="coord_n" exp="" desc=""/>
    <constraint field="observation" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column hidden="0" name="OGC_FID" width="-1" type="field"/>
      <column hidden="0" name="source" width="-1" type="field"/>
      <column hidden="0" name="genre" width="-1" type="field"/>
      <column hidden="0" name="coord_e" width="-1" type="field"/>
      <column hidden="0" name="coord_n" width="-1" type="field"/>
      <column hidden="0" name="observation" width="-1" type="field"/>
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
    <field editable="1" name="coord_e"/>
    <field editable="1" name="coord_n"/>
    <field editable="1" name="genre"/>
    <field editable="1" name="observation"/>
    <field editable="1" name="source"/>
  </editable>
  <labelOnTop>
    <field name="OGC_FID" labelOnTop="0"/>
    <field name="coord_e" labelOnTop="0"/>
    <field name="coord_n" labelOnTop="0"/>
    <field name="genre" labelOnTop="0"/>
    <field name="observation" labelOnTop="0"/>
    <field name="source" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
