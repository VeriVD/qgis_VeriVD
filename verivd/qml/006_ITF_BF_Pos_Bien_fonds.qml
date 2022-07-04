<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="1" minScale="2501" labelsEnabled="1" styleCategories="AllStyleCategories" maxScale="0" simplifyDrawingTol="1" simplifyAlgorithm="0" readOnly="0" version="3.4.4-Madeira" simplifyLocal="1" simplifyMaxScale="1" simplifyDrawingHints="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" type="singleSymbol" enableorderby="0" forceraster="0">
    <symbols>
      <symbol force_rhr="0" name="0" type="marker" alpha="1" clip_to_extent="1">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop v="0" k="angle"/>
          <prop v="170,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="area" k="scale_method"/>
          <prop v="0" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
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
  <labeling type="simple">
    <settings>
      <text-style useSubstitutions="0" fontWeight="50" namedStyle="Regular Condensed" fontSizeUnit="Point" blendMode="0" fontSize="12.5" fontStrikeout="0" textColor="0,0,0,255" fontWordSpacing="0" fontCapitals="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fieldName="number" previewBkgrdColor="#000000" multilineHeight="1" fontItalic="0" isExpression="0" fontFamily="Cadastra" textOpacity="1" fontLetterSpacing="0">
        <text-buffer bufferSizeUnits="MM" bufferJoinStyle="64" bufferBlendMode="0" bufferNoFill="0" bufferDraw="0" bufferColor="255,255,255,255" bufferOpacity="1" bufferSize="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0"/>
        <background shapeType="0" shapeOffsetY="0" shapeRotationType="0" shapeJoinStyle="64" shapeDraw="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiUnit="MM" shapeOffsetX="0" shapeOpacity="1" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeRadiiY="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidth="0" shapeSVGFile="" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeFillColor="255,255,255,255" shapeBorderWidthUnit="MM" shapeOffsetUnit="MM" shapeSizeType="0" shapeSizeY="0" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeSizeX="0" shapeRadiiX="0"/>
        <shadow shadowOffsetGlobal="1" shadowScale="100" shadowUnder="0" shadowColor="0,0,0,255" shadowOffsetUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowRadius="1.5" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowRadiusUnit="MM" shadowOffsetAngle="135" shadowOpacity="0.7" shadowRadiusAlphaOnly="0" shadowOffsetDist="1"/>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" decimals="3" formatNumbers="0" autoWrapLength="0" multilineAlign="0" addDirectionSymbol="0" plussign="0" rightDirectionSymbol=">" wrapChar="" leftDirectionSymbol="&lt;" placeDirectionSymbol="0" reverseDirectionSymbol="0"/>
      <placement predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" xOffset="0" quadOffset="4" preserveRotation="1" repeatDistance="0" fitInPolygonOnly="0" centroidWhole="0" offsetType="0" maxCurvedCharAngleOut="-20" yOffset="0" dist="0" placement="1" distUnits="MM" distMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" placementFlags="0" repeatDistanceUnits="MM" offsetUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="20" priority="5" rotationAngle="0" centroidInside="0"/>
      <rendering fontLimitPixelSize="0" scaleVisibility="1" fontMinPixelSize="3" maxNumLabels="2000" upsidedownLabels="0" mergeLines="0" scaleMin="1" minFeatureSize="0" zIndex="0" fontMaxPixelSize="10000" obstacle="1" limitNumLabels="0" displayAll="0" obstacleType="0" obstacleFactor="1" drawLabels="1" scaleMax="5000" labelPerPart="0"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" value="" type="QString"/>
          <Option name="properties" type="Map">
            <Option name="LabelRotation" type="Map">
              <Option name="active" value="true" type="bool"/>
              <Option name="expression" value="360 - ((90 - (ORI * 9 / 10)))" type="QString"/>
              <Option name="type" value="3" type="int"/>
            </Option>
          </Option>
          <Option name="type" value="collection" type="QString"/>
        </Option>
      </dd_properties>
    </settings>
  </labeling>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory barWidth="5" minScaleDenominator="0" enabled="0" height="15" penColor="#000000" width="15" sizeType="MM" labelPlacementMethod="XHeight" rotationOffset="270" scaleBasedVisibility="0" lineSizeType="MM" sizeScale="3x:0,0,0,0,0,0" lineSizeScale="3x:0,0,0,0,0,0" penWidth="0" scaleDependency="Area" backgroundColor="#ffffff" diagramOrientation="Up" minimumSize="0" penAlpha="255" backgroundAlpha="255" maxScaleDenominator="1e+08" opacity="1">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" field="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" showAll="1" linePlacementFlags="18" placement="0" zIndex="0" obstacle="0" dist="0">
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
    <field name="xtf_id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="posnumber_of">
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
    <field name="number">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ori">
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
    <alias name="" field="xtf_id" index="1"/>
    <alias name="" field="posnumber_of" index="2"/>
    <alias name="" field="identdn" index="3"/>
    <alias name="" field="number" index="4"/>
    <alias name="" field="ori" index="5"/>
    <alias name="" field="coord_e" index="6"/>
    <alias name="" field="coord_n" index="7"/>
    <alias name="" field="observation" index="8"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="OGC_FID" applyOnUpdate="0" expression=""/>
    <default field="xtf_id" applyOnUpdate="0" expression=""/>
    <default field="posnumber_of" applyOnUpdate="0" expression=""/>
    <default field="identdn" applyOnUpdate="0" expression=""/>
    <default field="number" applyOnUpdate="0" expression=""/>
    <default field="ori" applyOnUpdate="0" expression=""/>
    <default field="coord_e" applyOnUpdate="0" expression=""/>
    <default field="coord_n" applyOnUpdate="0" expression=""/>
    <default field="observation" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint notnull_strength="1" field="OGC_FID" unique_strength="1" constraints="3" exp_strength="0"/>
    <constraint notnull_strength="0" field="xtf_id" unique_strength="0" constraints="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="posnumber_of" unique_strength="0" constraints="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="identdn" unique_strength="0" constraints="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="number" unique_strength="0" constraints="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="ori" unique_strength="0" constraints="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="coord_e" unique_strength="0" constraints="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="coord_n" unique_strength="0" constraints="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="observation" unique_strength="0" constraints="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="OGC_FID"/>
    <constraint desc="" exp="" field="xtf_id"/>
    <constraint desc="" exp="" field="posnumber_of"/>
    <constraint desc="" exp="" field="identdn"/>
    <constraint desc="" exp="" field="number"/>
    <constraint desc="" exp="" field="ori"/>
    <constraint desc="" exp="" field="coord_e"/>
    <constraint desc="" exp="" field="coord_n"/>
    <constraint desc="" exp="" field="observation"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="">
    <columns>
      <column name="OGC_FID" type="field" hidden="0" width="-1"/>
      <column name="xtf_id" type="field" hidden="0" width="-1"/>
      <column name="posnumber_of" type="field" hidden="0" width="-1"/>
      <column name="identdn" type="field" hidden="0" width="-1"/>
      <column name="number" type="field" hidden="0" width="-1"/>
      <column name="ori" type="field" hidden="0" width="-1"/>
      <column name="coord_e" type="field" hidden="0" width="-1"/>
      <column name="coord_n" type="field" hidden="0" width="-1"/>
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
    <field editable="1" name="OGC_FID"/>
    <field editable="1" name="coord_e"/>
    <field editable="1" name="coord_n"/>
    <field editable="1" name="identdn"/>
    <field editable="1" name="number"/>
    <field editable="1" name="observation"/>
    <field editable="1" name="ori"/>
    <field editable="1" name="posnumber_of"/>
    <field editable="1" name="xtf_id"/>
  </editable>
  <labelOnTop>
    <field name="OGC_FID" labelOnTop="0"/>
    <field name="coord_e" labelOnTop="0"/>
    <field name="coord_n" labelOnTop="0"/>
    <field name="identdn" labelOnTop="0"/>
    <field name="number" labelOnTop="0"/>
    <field name="observation" labelOnTop="0"/>
    <field name="ori" labelOnTop="0"/>
    <field name="posnumber_of" labelOnTop="0"/>
    <field name="xtf_id" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
