<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" minScale="10000" simplifyAlgorithm="0" simplifyDrawingHints="0" simplifyMaxScale="1" styleCategories="AllStyleCategories" simplifyLocal="1" simplifyDrawingTol="1" hasScaleBasedVisibilityFlag="0" labelsEnabled="1" readOnly="0" version="3.8.2-Zanzibar">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" enableorderby="0" forceraster="0" type="RuleRenderer">
    <rules key="{133978cc-fd0d-40a1-9dbc-c368eef6ccf9}">
      <rule checkstate="0" symbol="0" key="{9d55d3c0-ffda-4dca-88a1-3f7517a30714}" filter="  &quot;numero_itf&quot; LIKE '%DP%' AND  &quot;numero_dwh&quot; LIKE '%DP%'" label="DP - DP"/>
      <rule symbol="1" key="{7d239930-6fd4-4f07-ba11-55a26b1db66a}" filter="  &quot;numero_itf&quot; NOT LIKE '%DP%' OR  &quot;numero_dwh&quot; NOT LIKE '%DP%'" label="DP - Privé ou Privé - Privé"/>
    </rules>
    <symbols>
      <symbol alpha="1" force_rhr="0" type="marker" name="0" clip_to_extent="1">
        <layer enabled="1" locked="0" class="SimpleMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="231,113,72,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="3" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" force_rhr="0" type="marker" name="1" clip_to_extent="1">
        <layer enabled="1" locked="0" class="SimpleMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="190,207,80,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="3" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
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
  </renderer-v2>
  <labeling type="simple">
    <settings>
      <text-style fontUnderline="0" fontSizeUnit="Point" multilineHeight="1" fontWeight="50" useSubstitutions="0" namedStyle="Regular" fontStrikeout="0" fontWordSpacing="0" fontSize="10" fieldName="  concat('ITF : ', &quot;numero_itf&quot; ,  '\n' , 'BDCO : ', &quot;numero_dwh&quot; )" fontItalic="0" blendMode="0" previewBkgrdColor="#ffffff" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textColor="0,0,0,255" isExpression="1" textOpacity="1" fontLetterSpacing="0" fontFamily="Cadastra Cn" fontCapitals="0">
        <text-buffer bufferNoFill="1" bufferSize="1" bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferBlendMode="0" bufferOpacity="1"/>
        <background shapeOffsetY="0" shapeFillColor="255,255,255,255" shapeSizeX="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeType="0" shapeRadiiX="0" shapeOffsetUnit="MM" shapeOffsetX="0" shapeJoinStyle="64" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeRadiiUnit="MM" shapeBorderWidth="0" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeSizeType="0" shapeRotation="0" shapeOpacity="1" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeSizeY="0" shapeSVGFile="" shapeDraw="0"/>
        <shadow shadowOffsetUnit="MM" shadowRadius="1.5" shadowScale="100" shadowOffsetAngle="135" shadowBlendMode="6" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowColor="0,0,0,255" shadowOffsetDist="1" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowDraw="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowRadiusUnit="MM" shadowOffsetGlobal="1"/>
        <substitutions/>
      </text-style>
      <text-format placeDirectionSymbol="0" plussign="0" addDirectionSymbol="0" autoWrapLength="0" reverseDirectionSymbol="0" formatNumbers="0" wrapChar="" leftDirectionSymbol="&lt;" useMaxLineLengthForAutoWrap="1" decimals="3" multilineAlign="3" rightDirectionSymbol=">"/>
      <placement dist="0" distMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" repeatDistance="0" offsetUnits="MM" yOffset="0" repeatDistanceUnits="MM" xOffset="0" geometryGenerator="" rotationAngle="0" placementFlags="10" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorEnabled="0" fitInPolygonOnly="0" centroidInside="0" maxCurvedCharAngleIn="25" preserveRotation="1" centroidWhole="0" maxCurvedCharAngleOut="-25" offsetType="0" priority="5" placement="1" quadOffset="4" distUnits="MM" labelOffsetMapUnitScale="3x:0,0,0,0,0,0"/>
      <rendering mergeLines="0" obstacle="1" labelPerPart="0" scaleMin="0" obstacleType="0" limitNumLabels="0" fontMaxPixelSize="10000" displayAll="0" fontLimitPixelSize="0" minFeatureSize="0" scaleVisibility="1" obstacleFactor="1" scaleMax="2000" zIndex="0" fontMinPixelSize="3" upsidedownLabels="0" maxNumLabels="2000" drawLabels="1"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" type="QString" name="name"/>
          <Option name="properties"/>
          <Option value="collection" type="QString" name="type"/>
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
    <DiagramCategory penWidth="0" lineSizeScale="3x:0,0,0,0,0,0" diagramOrientation="Up" enabled="0" minimumSize="0" width="15" opacity="1" penColor="#000000" labelPlacementMethod="XHeight" minScaleDenominator="0" lineSizeType="MM" sizeScale="3x:0,0,0,0,0,0" maxScaleDenominator="1e+08" backgroundAlpha="255" rotationOffset="270" height="15" penAlpha="255" sizeType="MM" scaleDependency="Area" barWidth="5" scaleBasedVisibility="0" backgroundColor="#ffffff">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings zIndex="0" dist="0" showAll="1" priority="0" obstacle="0" placement="0" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
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
    <field name="numero_itf">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="numero_dwh">
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
    <alias field="numero_itf" index="1" name=""/>
    <alias field="numero_dwh" index="2" name=""/>
    <alias field="coord_e" index="3" name=""/>
    <alias field="coord_n" index="4" name=""/>
    <alias field="observation" index="5" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="OGC_FID" applyOnUpdate="0" expression=""/>
    <default field="numero_itf" applyOnUpdate="0" expression=""/>
    <default field="numero_dwh" applyOnUpdate="0" expression=""/>
    <default field="coord_e" applyOnUpdate="0" expression=""/>
    <default field="coord_n" applyOnUpdate="0" expression=""/>
    <default field="observation" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint field="OGC_FID" unique_strength="1" exp_strength="0" notnull_strength="1" constraints="3"/>
    <constraint field="numero_itf" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="numero_dwh" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="coord_e" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="coord_n" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="observation" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="OGC_FID" exp="" desc=""/>
    <constraint field="numero_itf" exp="" desc=""/>
    <constraint field="numero_dwh" exp="" desc=""/>
    <constraint field="coord_e" exp="" desc=""/>
    <constraint field="coord_n" exp="" desc=""/>
    <constraint field="observation" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column hidden="0" width="-1" type="field" name="OGC_FID"/>
      <column hidden="0" width="-1" type="field" name="numero_itf"/>
      <column hidden="0" width="-1" type="field" name="numero_dwh"/>
      <column hidden="0" width="-1" type="field" name="coord_e"/>
      <column hidden="0" width="-1" type="field" name="coord_n"/>
      <column hidden="0" width="-1" type="field" name="observation"/>
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
    <field editable="1" name="numero_dwh"/>
    <field editable="1" name="numero_itf"/>
    <field editable="1" name="observation"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="OGC_FID"/>
    <field labelOnTop="0" name="coord_e"/>
    <field labelOnTop="0" name="coord_n"/>
    <field labelOnTop="0" name="numero_dwh"/>
    <field labelOnTop="0" name="numero_itf"/>
    <field labelOnTop="0" name="observation"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
