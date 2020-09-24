<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" simplifyDrawingHints="1" styleCategories="AllStyleCategories" minScale="1e+08" simplifyAlgorithm="0" simplifyLocal="1" hasScaleBasedVisibilityFlag="0" labelsEnabled="0" simplifyDrawingTol="1" maxScale="0" version="3.4.4-Madeira" simplifyMaxScale="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" symbollevels="0" forceraster="0" type="singleSymbol">
    <symbols>
      <symbol clip_to_extent="1" force_rhr="0" type="fill" name="0" alpha="1">
        <layer locked="0" pass="0" enabled="1" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,0,17,255" k="outline_color"/>
          <prop v="dash" k="outline_style"/>
          <prop v="2" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="no" k="style"/>
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
    <DiagramCategory opacity="1" lineSizeType="MM" lineSizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" barWidth="5" sizeScale="3x:0,0,0,0,0,0" enabled="0" penColor="#000000" maxScaleDenominator="1e+08" diagramOrientation="Up" penWidth="0" sizeType="MM" scaleDependency="Area" minimumSize="0" scaleBasedVisibility="0" height="15" penAlpha="255" width="15" backgroundAlpha="255" rotationOffset="270" minScaleDenominator="0" labelPlacementMethod="XHeight">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" showAll="1" zIndex="0" linePlacementFlags="18" dist="0" placement="1" priority="0">
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
    <field name="nom">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="noofs">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="numcom">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="no_district">
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
    <alias field="OGC_FID" name="" index="0"/>
    <alias field="nom" name="" index="1"/>
    <alias field="noofs" name="" index="2"/>
    <alias field="numcom" name="" index="3"/>
    <alias field="no_district" name="" index="4"/>
    <alias field="observation" name="" index="5"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="OGC_FID" expression="" applyOnUpdate="0"/>
    <default field="nom" expression="" applyOnUpdate="0"/>
    <default field="noofs" expression="" applyOnUpdate="0"/>
    <default field="numcom" expression="" applyOnUpdate="0"/>
    <default field="no_district" expression="" applyOnUpdate="0"/>
    <default field="observation" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint constraints="3" field="OGC_FID" exp_strength="0" unique_strength="1" notnull_strength="1"/>
    <constraint constraints="0" field="nom" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="noofs" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="numcom" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="no_district" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="observation" exp_strength="0" unique_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="OGC_FID"/>
    <constraint exp="" desc="" field="nom"/>
    <constraint exp="" desc="" field="noofs"/>
    <constraint exp="" desc="" field="numcom"/>
    <constraint exp="" desc="" field="no_district"/>
    <constraint exp="" desc="" field="observation"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="">
    <columns>
      <column width="-1" type="field" name="OGC_FID" hidden="0"/>
      <column width="-1" type="field" name="nom" hidden="0"/>
      <column width="-1" type="field" name="noofs" hidden="0"/>
      <column width="-1" type="field" name="numcom" hidden="0"/>
      <column width="-1" type="field" name="no_district" hidden="0"/>
      <column width="-1" type="field" name="observation" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
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
    <field editable="1" name="no_district"/>
    <field editable="1" name="nom"/>
    <field editable="1" name="noofs"/>
    <field editable="1" name="numcom"/>
    <field editable="1" name="observation"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="OGC_FID"/>
    <field labelOnTop="0" name="no_district"/>
    <field labelOnTop="0" name="nom"/>
    <field labelOnTop="0" name="noofs"/>
    <field labelOnTop="0" name="numcom"/>
    <field labelOnTop="0" name="observation"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
