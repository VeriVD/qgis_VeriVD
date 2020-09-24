<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" simplifyDrawingHints="1" styleCategories="AllStyleCategories" minScale="1e+08" simplifyAlgorithm="0" simplifyLocal="1" hasScaleBasedVisibilityFlag="0" labelsEnabled="0" simplifyDrawingTol="1" maxScale="0" version="3.4.4-Madeira" simplifyMaxScale="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" symbollevels="0" forceraster="0" type="singleSymbol">
    <symbols>
      <symbol clip_to_extent="1" force_rhr="0" type="line" name="0" alpha="1">
        <layer locked="0" pass="0" enabled="1" class="GeometryGenerator">
          <prop v="Line" k="SymbolType"/>
          <prop v="difference(&#xd;&#xa;    difference( &#xd;&#xa;        $geometry,&#xd;&#xa;        buffer( start_point( $geometry),5)&#xd;&#xa;    ),&#xd;&#xa;&#x9;buffer( end_point( $geometry),5)&#xd;&#xa;)&#x9;" k="geometryModifier"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" type="line" name="@0@0" alpha="1">
            <layer locked="0" pass="0" enabled="1" class="ArrowLine">
              <prop v="1" k="arrow_start_width"/>
              <prop v="MM" k="arrow_start_width_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
              <prop v="0" k="arrow_type"/>
              <prop v="2" k="arrow_width"/>
              <prop v="MM" k="arrow_width_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
              <prop v="1.5" k="head_length"/>
              <prop v="MM" k="head_length_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
              <prop v="1.5" k="head_thickness"/>
              <prop v="MM" k="head_thickness_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
              <prop v="2" k="head_type"/>
              <prop v="1" k="is_curved"/>
              <prop v="1" k="is_repeated"/>
              <prop v="0" k="offset"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
              <prop v="0" k="ring_filter"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
              <symbol clip_to_extent="1" force_rhr="0" type="fill" name="@@0@0@0" alpha="1">
                <layer locked="0" pass="0" enabled="1" class="SimpleFill">
                  <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
                  <prop v="255,55,58,255" k="color"/>
                  <prop v="miter" k="joinstyle"/>
                  <prop v="0,0" k="offset"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MM" k="offset_unit"/>
                  <prop v="35,35,35,255" k="outline_color"/>
                  <prop v="solid" k="outline_style"/>
                  <prop v="0.26" k="outline_width"/>
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
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions">
      <value>OGC_FID</value>
    </property>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>0.506</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory opacity="1" lineSizeType="MM" lineSizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" barWidth="5" sizeScale="3x:0,0,0,0,0,0" enabled="0" penColor="#000000" maxScaleDenominator="1e+08" diagramOrientation="Up" penWidth="0" sizeType="MM" scaleDependency="Area" minimumSize="0" scaleBasedVisibility="0" height="15" penAlpha="255" width="15" backgroundAlpha="255" rotationOffset="270" minScaleDenominator="0" labelPlacementMethod="XHeight">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" field="" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" showAll="1" zIndex="0" linePlacementFlags="18" dist="0" placement="2" priority="0">
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
    <field name="numero">
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
    <field name="numeroplan">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="numerodoublon">
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
    <alias field="source" name="" index="1"/>
    <alias field="genre" name="" index="2"/>
    <alias field="numero" name="" index="3"/>
    <alias field="numcom" name="" index="4"/>
    <alias field="numeroplan" name="" index="5"/>
    <alias field="numerodoublon" name="" index="6"/>
    <alias field="observation" name="" index="7"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="OGC_FID" expression="" applyOnUpdate="0"/>
    <default field="source" expression="" applyOnUpdate="0"/>
    <default field="genre" expression="" applyOnUpdate="0"/>
    <default field="numero" expression="" applyOnUpdate="0"/>
    <default field="numcom" expression="" applyOnUpdate="0"/>
    <default field="numeroplan" expression="" applyOnUpdate="0"/>
    <default field="numerodoublon" expression="" applyOnUpdate="0"/>
    <default field="observation" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint constraints="3" field="OGC_FID" exp_strength="0" unique_strength="1" notnull_strength="1"/>
    <constraint constraints="0" field="source" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="genre" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="numero" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="numcom" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="numeroplan" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="numerodoublon" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="observation" exp_strength="0" unique_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="OGC_FID"/>
    <constraint exp="" desc="" field="source"/>
    <constraint exp="" desc="" field="genre"/>
    <constraint exp="" desc="" field="numero"/>
    <constraint exp="" desc="" field="numcom"/>
    <constraint exp="" desc="" field="numeroplan"/>
    <constraint exp="" desc="" field="numerodoublon"/>
    <constraint exp="" desc="" field="observation"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="">
    <columns>
      <column width="-1" type="field" name="OGC_FID" hidden="0"/>
      <column width="-1" type="field" name="source" hidden="0"/>
      <column width="-1" type="field" name="genre" hidden="0"/>
      <column width="-1" type="field" name="numero" hidden="0"/>
      <column width="-1" type="field" name="numcom" hidden="0"/>
      <column width="-1" type="field" name="numeroplan" hidden="0"/>
      <column width="-1" type="field" name="numerodoublon" hidden="0"/>
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
    <field editable="1" name="genre"/>
    <field editable="1" name="numcom"/>
    <field editable="1" name="numero"/>
    <field editable="1" name="numerodoublon"/>
    <field editable="1" name="numeroplan"/>
    <field editable="1" name="observation"/>
    <field editable="1" name="source"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="OGC_FID"/>
    <field labelOnTop="0" name="genre"/>
    <field labelOnTop="0" name="numcom"/>
    <field labelOnTop="0" name="numero"/>
    <field labelOnTop="0" name="numerodoublon"/>
    <field labelOnTop="0" name="numeroplan"/>
    <field labelOnTop="0" name="observation"/>
    <field labelOnTop="0" name="source"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
