<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="1" hasScaleBasedVisibilityFlag="1" simplifyMaxScale="1" version="3.4.4-Madeira" simplifyLocal="1" readOnly="0" styleCategories="AllStyleCategories" simplifyAlgorithm="0" simplifyDrawingTol="1" minScale="2500" maxScale="0" simplifyDrawingHints="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" forceraster="0" symbollevels="0" type="singleSymbol">
    <symbols>
      <symbol name="0" clip_to_extent="1" force_rhr="0" alpha="1" type="marker">
        <layer pass="0" locked="0" enabled="1" class="SimpleMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,0,0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="cross2"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="area"/>
          <prop k="size" v="0"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
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
      <text-style fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontLetterSpacing="0" fontStrikeout="0" fontSize="8.25" fontWeight="50" textOpacity="1" fontUnderline="0" useSubstitutions="0" fontCapitals="0" namedStyle="Normal" fontWordSpacing="0" fontFamily="MS Shell Dlg 2" isExpression="0" fontSizeUnit="Point" multilineHeight="1" textColor="0,0,0,255" previewBkgrdColor="#ffffff" fontItalic="0" fieldName="name" blendMode="0">
        <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferJoinStyle="64" bufferOpacity="1" bufferSizeUnits="MM" bufferNoFill="0" bufferSize="1" bufferColor="255,220,255,255" bufferBlendMode="0"/>
        <background shapeSizeType="0" shapeSizeY="0" shapeRadiiX="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetY="0" shapeOffsetX="0" shapeOffsetUnit="MM" shapeDraw="0" shapeRadiiUnit="MM" shapeType="0" shapeRadiiY="0" shapeRotationType="0" shapeOpacity="1" shapeSizeUnit="MM" shapeSVGFile="" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeBlendMode="0" shapeBorderWidthUnit="MM" shapeJoinStyle="64" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeSizeX="0" shapeRotation="0" shapeBorderWidth="0"/>
        <shadow shadowColor="0,0,0,255" shadowRadiusAlphaOnly="0" shadowUnder="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowOffsetGlobal="1" shadowDraw="0" shadowRadius="1.5" shadowScale="100" shadowOffsetUnit="MM" shadowRadiusUnit="MM" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOpacity="0.7" shadowBlendMode="6" shadowOffsetDist="1"/>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" rightDirectionSymbol=">" decimals="3" reverseDirectionSymbol="0" wrapChar="" plussign="0" multilineAlign="0" leftDirectionSymbol="&lt;" autoWrapLength="0" placeDirectionSymbol="0" formatNumbers="0"/>
      <placement repeatDistance="0" priority="5" distMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" offsetType="0" maxCurvedCharAngleIn="20" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" distUnits="MM" centroidWhole="0" placementFlags="0" xOffset="0" yOffset="0" maxCurvedCharAngleOut="-20" quadOffset="4" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" placement="1" offsetUnits="MM" fitInPolygonOnly="0" centroidInside="0" repeatDistanceUnits="MM" dist="0" rotationAngle="0" preserveRotation="1"/>
      <rendering drawLabels="1" upsidedownLabels="0" zIndex="0" fontMinPixelSize="3" obstacleType="0" limitNumLabels="0" fontMaxPixelSize="10000" obstacle="1" scaleVisibility="0" minFeatureSize="0" displayAll="0" labelPerPart="0" scaleMin="1" maxNumLabels="2000" scaleMax="10000000" mergeLines="0" obstacleFactor="1" fontLimitPixelSize="0"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" value="" type="QString"/>
          <Option name="properties" type="Map">
            <Option name="LabelRotation" type="Map">
              <Option name="active" value="true" type="bool"/>
              <Option name="expression" value="360 - (90 - Ori *  9/10)" type="QString"/>
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
    <DiagramCategory backgroundColor="#ffffff" diagramOrientation="Up" maxScaleDenominator="1e+08" width="15" rotationOffset="270" lineSizeScale="3x:0,0,0,0,0,0" scaleDependency="Area" penAlpha="255" minimumSize="0" height="15" labelPlacementMethod="XHeight" sizeType="MM" opacity="1" backgroundAlpha="255" penWidth="0" enabled="0" sizeScale="3x:0,0,0,0,0,0" lineSizeType="MM" penColor="#000000" minScaleDenominator="0" barWidth="5" scaleBasedVisibility="0">
      <fontProperties style="" description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" zIndex="0" linePlacementFlags="18" placement="0" showAll="1" priority="0" dist="0">
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
    <field name="posname_of">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="category">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="name">
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
    <alias field="OGC_FID" name="" index="0"/>
    <alias field="xtf_id" name="" index="1"/>
    <alias field="posname_of" name="" index="2"/>
    <alias field="category" name="" index="3"/>
    <alias field="name" name="" index="4"/>
    <alias field="ori" name="" index="5"/>
    <alias field="coord_e" name="" index="6"/>
    <alias field="coord_n" name="" index="7"/>
    <alias field="observation" name="" index="8"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="OGC_FID" expression="" applyOnUpdate="0"/>
    <default field="xtf_id" expression="" applyOnUpdate="0"/>
    <default field="posname_of" expression="" applyOnUpdate="0"/>
    <default field="category" expression="" applyOnUpdate="0"/>
    <default field="name" expression="" applyOnUpdate="0"/>
    <default field="ori" expression="" applyOnUpdate="0"/>
    <default field="coord_e" expression="" applyOnUpdate="0"/>
    <default field="coord_n" expression="" applyOnUpdate="0"/>
    <default field="observation" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint field="OGC_FID" exp_strength="0" constraints="3" unique_strength="1" notnull_strength="1"/>
    <constraint field="xtf_id" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="posname_of" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="category" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="name" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="ori" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="coord_e" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="coord_n" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="observation" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="OGC_FID" desc="" exp=""/>
    <constraint field="xtf_id" desc="" exp=""/>
    <constraint field="posname_of" desc="" exp=""/>
    <constraint field="category" desc="" exp=""/>
    <constraint field="name" desc="" exp=""/>
    <constraint field="ori" desc="" exp=""/>
    <constraint field="coord_e" desc="" exp=""/>
    <constraint field="coord_n" desc="" exp=""/>
    <constraint field="observation" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column name="OGC_FID" hidden="0" type="field" width="-1"/>
      <column name="xtf_id" hidden="0" type="field" width="-1"/>
      <column name="posname_of" hidden="0" type="field" width="-1"/>
      <column name="category" hidden="0" type="field" width="-1"/>
      <column name="name" hidden="0" type="field" width="-1"/>
      <column name="ori" hidden="0" type="field" width="-1"/>
      <column name="coord_e" hidden="0" type="field" width="-1"/>
      <column name="coord_n" hidden="0" type="field" width="-1"/>
      <column name="observation" hidden="0" type="field" width="-1"/>
      <column hidden="1" type="actions" width="-1"/>
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
    <field name="OGC_FID" editable="1"/>
    <field name="category" editable="1"/>
    <field name="coord_e" editable="1"/>
    <field name="coord_n" editable="1"/>
    <field name="name" editable="1"/>
    <field name="observation" editable="1"/>
    <field name="ori" editable="1"/>
    <field name="posname_of" editable="1"/>
    <field name="xtf_id" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="OGC_FID" labelOnTop="0"/>
    <field name="category" labelOnTop="0"/>
    <field name="coord_e" labelOnTop="0"/>
    <field name="coord_n" labelOnTop="0"/>
    <field name="name" labelOnTop="0"/>
    <field name="observation" labelOnTop="0"/>
    <field name="ori" labelOnTop="0"/>
    <field name="posname_of" labelOnTop="0"/>
    <field name="xtf_id" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>posname_of</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
