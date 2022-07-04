<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyAlgorithm="0" simplifyMaxScale="1" simplifyLocal="1" minScale="1e+08" hasScaleBasedVisibilityFlag="0" maxScale="300" simplifyDrawingHints="1" version="3.4.4-Madeira" labelsEnabled="1" styleCategories="AllStyleCategories" readOnly="0" simplifyDrawingTol="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" type="categorizedSymbol" symbollevels="0" attr="Genre" forceraster="0">
    <categories>
      <category label="batiment_souterrain" value="batiment_souterrain" symbol="0" render="true"/>
      <category label="couvert_independant" value="couvert_independant" symbol="1" render="true"/>
    </categories>
    <symbols>
      <symbol name="0" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer enabled="1" pass="0" class="SimpleLine" locked="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="228,26,28,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="3" k="line_width"/>
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
      <symbol name="1" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer enabled="1" pass="0" class="SimpleLine" locked="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="228,26,28,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="3" k="line_width"/>
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
    <source-symbol>
      <symbol name="0" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer enabled="1" pass="0" class="SimpleFill" locked="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="213,180,60,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
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
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
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
      <text-style fontUnderline="0" blendMode="0" textColor="0,0,0,255" previewBkgrdColor="#ffffff" fontFamily="MS Shell Dlg 2" namedStyle="Normal" fontWeight="50" fontSize="10" fontSizeUnit="Point" multilineHeight="1" useSubstitutions="0" fontCapitals="0" textOpacity="1" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWordSpacing="0" fontItalic="0" fieldName="'Genre = ' +  replace(  &quot;Genre&quot; , '_', '  ')  +  '\n'  + '&amp;' +  '\n'  +'Designation = ' +   substr(  &quot;Designation&quot; ,strpos(&quot;Designation&quot;,'.')+1,50) " fontStrikeout="0" isExpression="1" fontLetterSpacing="0">
        <text-buffer bufferColor="255,255,255,255" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferBlendMode="0" bufferSize="1" bufferDraw="1" bufferNoFill="1" bufferSizeUnits="MM" bufferJoinStyle="128"/>
        <background shapeType="0" shapeRadiiX="0" shapeJoinStyle="64" shapeRotation="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeSizeX="0" shapeOffsetY="0" shapeBorderWidthUnit="MM" shapeBorderWidth="0" shapeRadiiY="0" shapeDraw="0" shapeSizeUnit="MM" shapeOffsetUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeType="0" shapeFillColor="255,255,255,255" shapeSizeY="0" shapeSVGFile="" shapeRadiiUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeRotationType="0" shapeOffsetX="0"/>
        <shadow shadowDraw="0" shadowUnder="0" shadowBlendMode="6" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowOpacity="0.7" shadowColor="0,0,0,255" shadowRadiusUnit="MM" shadowRadius="1.5" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowRadiusAlphaOnly="0"/>
        <substitutions/>
      </text-style>
      <text-format autoWrapLength="0" plussign="0" addDirectionSymbol="0" formatNumbers="0" leftDirectionSymbol="&lt;" decimals="3" useMaxLineLengthForAutoWrap="1" reverseDirectionSymbol="0" placeDirectionSymbol="0" wrapChar="" rightDirectionSymbol=">" multilineAlign="1"/>
      <placement placementFlags="10" distUnits="MM" offsetType="0" yOffset="0" placement="1" repeatDistance="0" fitInPolygonOnly="0" centroidInside="0" priority="5" maxCurvedCharAngleOut="-25" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" xOffset="0" preserveRotation="1" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceUnits="MM" offsetUnits="MM" quadOffset="4" rotationAngle="0" dist="0" maxCurvedCharAngleIn="25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" centroidWhole="0"/>
      <rendering labelPerPart="0" mergeLines="0" fontLimitPixelSize="0" minFeatureSize="0" scaleVisibility="1" obstacleType="0" upsidedownLabels="0" drawLabels="1" maxNumLabels="2000" scaleMax="300" fontMinPixelSize="3" limitNumLabels="0" scaleMin="0" obstacle="1" fontMaxPixelSize="10000" obstacleFactor="1" displayAll="1" zIndex="0"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" type="QString" value=""/>
          <Option name="properties"/>
          <Option name="type" type="QString" value="collection"/>
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
    <DiagramCategory penWidth="0" diagramOrientation="Up" sizeScale="3x:0,0,0,0,0,0" minScaleDenominator="300" scaleDependency="Area" minimumSize="0" rotationOffset="270" maxScaleDenominator="1e+08" backgroundAlpha="255" scaleBasedVisibility="0" lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" lineSizeType="MM" width="15" opacity="1" penColor="#000000" penAlpha="255" sizeType="MM" barWidth="5" enabled="0" height="15" backgroundColor="#ffffff">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" field="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings showAll="1" priority="0" linePlacementFlags="18" obstacle="0" zIndex="0" placement="1" dist="0">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
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
    <field name="designation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="designation_incorrect">
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
    <alias name="" field="genre" index="1"/>
    <alias name="" field="numero" index="2"/>
    <alias name="" field="designation" index="3"/>
    <alias name="" field="designation_incorrect" index="4"/>
    <alias name="" field="observation" index="5"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="OGC_FID" applyOnUpdate="0" expression=""/>
    <default field="genre" applyOnUpdate="0" expression=""/>
    <default field="numero" applyOnUpdate="0" expression=""/>
    <default field="designation" applyOnUpdate="0" expression=""/>
    <default field="designation_incorrect" applyOnUpdate="0" expression=""/>
    <default field="observation" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" field="OGC_FID" constraints="3" unique_strength="1" notnull_strength="1"/>
    <constraint exp_strength="0" field="genre" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint exp_strength="0" field="numero" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint exp_strength="0" field="designation" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint exp_strength="0" field="designation_incorrect" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint exp_strength="0" field="observation" constraints="0" unique_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="OGC_FID" desc=""/>
    <constraint exp="" field="genre" desc=""/>
    <constraint exp="" field="numero" desc=""/>
    <constraint exp="" field="designation" desc=""/>
    <constraint exp="" field="designation_incorrect" desc=""/>
    <constraint exp="" field="observation" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column width="-1" type="actions" hidden="1"/>
      <column width="-1" name="OGC_FID" type="field" hidden="0"/>
      <column width="-1" name="genre" type="field" hidden="0"/>
      <column width="-1" name="numero" type="field" hidden="0"/>
      <column width="-1" name="designation" type="field" hidden="0"/>
      <column width="-1" name="designation_incorrect" type="field" hidden="0"/>
      <column width="-1" name="observation" type="field" hidden="0"/>
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
    <field name="OGC_FID" editable="1"/>
    <field name="PRIMARYINDEX" editable="1"/>
    <field name="designation" editable="1"/>
    <field name="designation_incorrect" editable="1"/>
    <field name="genre" editable="1"/>
    <field name="numero" editable="1"/>
    <field name="observation" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="Designation" labelOnTop="0"/>
    <field name="Designation_incorrect" labelOnTop="0"/>
    <field name="Genre" labelOnTop="0"/>
    <field name="Numero" labelOnTop="0"/>
    <field name="OGC_FID" labelOnTop="0"/>
    <field name="PRIMARYINDEX" labelOnTop="0"/>
    <field name="designation" labelOnTop="0"/>
    <field name="designation_incorrect" labelOnTop="0"/>
    <field name="genre" labelOnTop="0"/>
    <field name="numero" labelOnTop="0"/>
    <field name="observation" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>PRIMARYINDEX</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
