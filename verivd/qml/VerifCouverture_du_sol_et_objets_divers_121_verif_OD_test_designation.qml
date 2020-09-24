<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" simplifyAlgorithm="0" simplifyDrawingHints="1" simplifyDrawingTol="1" labelsEnabled="1" maxScale="300" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" simplifyMaxScale="1" version="3.4.4-Madeira" minScale="1e+08" simplifyLocal="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" symbollevels="0" attr="Genre" type="categorizedSymbol" enableorderby="0">
    <categories>
      <category value="batiment_souterrain" render="true" symbol="0" label="batiment_souterrain"/>
      <category value="couvert_independant" render="true" symbol="1" label="couvert_independant"/>
    </categories>
    <symbols>
      <symbol name="0" type="fill" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer pass="0" enabled="1" locked="0" class="SimpleLine">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="228,26,28,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="3"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="1" type="fill" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer pass="0" enabled="1" locked="0" class="SimpleLine">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="228,26,28,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="3"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
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
    <source-symbol>
      <symbol name="0" type="fill" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer pass="0" enabled="1" locked="0" class="SimpleFill">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="213,180,60,255"/>
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </source-symbol>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings>
      <text-style fontLetterSpacing="0" textColor="0,0,0,255" previewBkgrdColor="#ffffff" isExpression="1" fontFamily="MS Shell Dlg 2" useSubstitutions="0" fontSize="10" blendMode="0" fontCapitals="0" fontItalic="0" fontWordSpacing="0" fontUnderline="0" namedStyle="Normal" fontWeight="50" multilineHeight="1" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fieldName="'Genre = ' +  replace(  &quot;Genre&quot; , '_', '  ')  +  '\n'  + '&amp;' +  '\n'  +'Designation = ' +   substr(  &quot;Designation&quot; ,strpos(&quot;Designation&quot;,'.')+1,50) " fontStrikeout="0" textOpacity="1" fontSizeUnit="Point">
        <text-buffer bufferDraw="1" bufferNoFill="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSizeUnits="MM" bufferOpacity="1" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferSize="1" bufferBlendMode="0"/>
        <background shapeOffsetY="0" shapeSizeType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetUnit="MM" shapeDraw="0" shapeSizeY="0" shapeBlendMode="0" shapeOpacity="1" shapeType="0" shapeOffsetX="0" shapeFillColor="255,255,255,255" shapeJoinStyle="64" shapeRotation="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeSizeX="0" shapeRadiiY="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeSVGFile="" shapeSizeUnit="MM" shapeBorderWidthUnit="MM" shapeBorderWidth="0" shapeRadiiUnit="MM" shapeBorderColor="128,128,128,255" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0"/>
        <shadow shadowRadius="1.5" shadowColor="0,0,0,255" shadowDraw="0" shadowRadiusAlphaOnly="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowUnder="0" shadowOffsetUnit="MM" shadowOpacity="0.7" shadowScale="100" shadowBlendMode="6" shadowOffsetGlobal="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetDist="1" shadowRadiusUnit="MM"/>
        <substitutions/>
      </text-style>
      <text-format multilineAlign="1" addDirectionSymbol="0" plussign="0" rightDirectionSymbol=">" autoWrapLength="0" wrapChar="" leftDirectionSymbol="&lt;" placeDirectionSymbol="0" decimals="3" useMaxLineLengthForAutoWrap="1" formatNumbers="0" reverseDirectionSymbol="0"/>
      <placement repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" offsetType="0" offsetUnits="MM" priority="5" repeatDistanceUnits="MM" placement="1" xOffset="0" yOffset="0" fitInPolygonOnly="0" quadOffset="4" repeatDistance="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" dist="0" centroidInside="0" centroidWhole="0" maxCurvedCharAngleIn="25" maxCurvedCharAngleOut="-25" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" rotationAngle="0" distMapUnitScale="3x:0,0,0,0,0,0" distUnits="MM"/>
      <rendering obstacleType="0" limitNumLabels="0" minFeatureSize="0" scaleMin="0" upsidedownLabels="0" maxNumLabels="2000" obstacle="1" displayAll="0" obstacleFactor="1" fontMinPixelSize="3" scaleVisibility="1" fontLimitPixelSize="0" zIndex="0" fontMaxPixelSize="10000" labelPerPart="0" scaleMax="300" drawLabels="1" mergeLines="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" name="name" type="QString"/>
          <Option name="properties"/>
          <Option value="collection" name="type" type="QString"/>
        </Option>
      </dd_properties>
    </settings>
  </labeling>
  <customproperties>
    <property key="dualview/previewExpressions" value="&quot;PRIMARYINDEX&quot;"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory backgroundAlpha="255" width="15" lineSizeScale="3x:0,0,0,0,0,0" penWidth="0" scaleDependency="Area" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" height="15" labelPlacementMethod="XHeight" enabled="0" diagramOrientation="Up" sizeScale="3x:0,0,0,0,0,0" penColor="#000000" minScaleDenominator="0" minimumSize="0" rotationOffset="270" sizeType="MM" backgroundColor="#ffffff" scaleBasedVisibility="0" lineSizeType="MM" opacity="1">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" zIndex="0" dist="0" showAll="1" linePlacementFlags="18" placement="1" obstacle="0">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="PRIMARYINDEX">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Genre">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Numero">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Designation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Designation_incorrect">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="PRIMARYINDEX" index="0" name=""/>
    <alias field="Genre" index="1" name=""/>
    <alias field="Numero" index="2" name=""/>
    <alias field="Designation" index="3" name=""/>
    <alias field="Designation_incorrect" index="4" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" field="PRIMARYINDEX" applyOnUpdate="0"/>
    <default expression="" field="Genre" applyOnUpdate="0"/>
    <default expression="" field="Numero" applyOnUpdate="0"/>
    <default expression="" field="Designation" applyOnUpdate="0"/>
    <default expression="" field="Designation_incorrect" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" exp_strength="0" notnull_strength="1" field="PRIMARYINDEX" constraints="3"/>
    <constraint unique_strength="0" exp_strength="0" notnull_strength="0" field="Genre" constraints="0"/>
    <constraint unique_strength="0" exp_strength="0" notnull_strength="0" field="Numero" constraints="0"/>
    <constraint unique_strength="0" exp_strength="0" notnull_strength="0" field="Designation" constraints="0"/>
    <constraint unique_strength="0" exp_strength="0" notnull_strength="0" field="Designation_incorrect" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="PRIMARYINDEX" desc="" exp=""/>
    <constraint field="Genre" desc="" exp=""/>
    <constraint field="Numero" desc="" exp=""/>
    <constraint field="Designation" desc="" exp=""/>
    <constraint field="Designation_incorrect" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="">
    <columns>
      <column width="-1" name="PRIMARYINDEX" type="field" hidden="0"/>
      <column width="-1" name="Genre" type="field" hidden="0"/>
      <column width="-1" name="Numero" type="field" hidden="0"/>
      <column width="-1" name="Designation" type="field" hidden="0"/>
      <column width="243" name="Designation_incorrect" type="field" hidden="0"/>
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
    <field name="Designation" editable="1"/>
    <field name="Designation_incorrect" editable="1"/>
    <field name="Genre" editable="1"/>
    <field name="Numero" editable="1"/>
    <field name="PRIMARYINDEX" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="Designation"/>
    <field labelOnTop="0" name="Designation_incorrect"/>
    <field labelOnTop="0" name="Genre"/>
    <field labelOnTop="0" name="Numero"/>
    <field labelOnTop="0" name="PRIMARYINDEX"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>PRIMARYINDEX</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
