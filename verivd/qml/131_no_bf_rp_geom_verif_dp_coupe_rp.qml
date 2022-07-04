<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyAlgorithm="0" simplifyDrawingHints="1" simplifyLocal="1" readOnly="0" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" simplifyDrawingTol="1" version="3.4.4-Madeira" maxScale="0" minScale="1e+08" labelsEnabled="0" simplifyMaxScale="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" forceraster="0" enableorderby="0" type="singleSymbol">
    <symbols>
      <symbol force_rhr="0" name="0" clip_to_extent="1" alpha="1" type="fill">
        <layer pass="0" enabled="1" class="SimpleFill" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="232,113,141,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
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
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory maxScaleDenominator="1e+08" barWidth="5" width="15" lineSizeType="MM" diagramOrientation="Up" enabled="0" sizeType="MM" opacity="1" penColor="#000000" penWidth="0" sizeScale="3x:0,0,0,0,0,0" minimumSize="0" penAlpha="255" height="15" labelPlacementMethod="XHeight" minScaleDenominator="0" scaleBasedVisibility="0" scaleDependency="Area" backgroundAlpha="255" lineSizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" rotationOffset="270">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings zIndex="0" dist="0" showAll="1" priority="0" obstacle="0" placement="1" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
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
    <field name="numero">
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
    <alias name="" index="1" field="numero"/>
    <alias name="" index="2" field="genre"/>
    <alias name="" index="3" field="observation"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" field="OGC_FID" expression=""/>
    <default applyOnUpdate="0" field="numero" expression=""/>
    <default applyOnUpdate="0" field="genre" expression=""/>
    <default applyOnUpdate="0" field="observation" expression=""/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" constraints="3" field="OGC_FID" unique_strength="1" notnull_strength="1"/>
    <constraint exp_strength="0" constraints="0" field="numero" unique_strength="0" notnull_strength="0"/>
    <constraint exp_strength="0" constraints="0" field="genre" unique_strength="0" notnull_strength="0"/>
    <constraint exp_strength="0" constraints="0" field="observation" unique_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="OGC_FID"/>
    <constraint exp="" desc="" field="numero"/>
    <constraint exp="" desc="" field="genre"/>
    <constraint exp="" desc="" field="observation"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" name="OGC_FID" hidden="0" type="field"/>
      <column width="-1" name="numero" hidden="0" type="field"/>
      <column width="-1" name="genre" hidden="0" type="field"/>
      <column width="-1" name="observation" hidden="0" type="field"/>
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
    <field editable="1" name="numero"/>
    <field editable="1" name="observation"/>
  </editable>
  <labelOnTop>
    <field name="OGC_FID" labelOnTop="0"/>
    <field name="genre" labelOnTop="0"/>
    <field name="numero" labelOnTop="0"/>
    <field name="observation" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
