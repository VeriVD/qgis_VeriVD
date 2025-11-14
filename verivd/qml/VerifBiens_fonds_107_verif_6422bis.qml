<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" simplifyAlgorithm="0" simplifyMaxScale="1" minScale="1e+08" readOnly="0" styleCategories="AllStyleCategories" version="3.8.2-Zanzibar" maxScale="0" simplifyDrawingTol="1" simplifyLocal="1" simplifyDrawingHints="1" labelsEnabled="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" enableorderby="0" type="RuleRenderer" forceraster="0">
    <rules key="{91bd870c-8302-4be1-b192-e1fbe8a575ef}">
      <rule symbol="0" key="{0238265d-b3ba-40bb-8800-31d53f8bf5dd}" label="vide"/>
      <rule filter="&quot;ecart&quot;  > 0 and  &quot;Tol_pourcent&quot; > 100" symbol="1" key="{fa5eee6a-cbe9-4b1b-ab63-80ea9e3a9a45}" label="Positif - Hors tolérance"/>
      <rule filter="&quot;ecart&quot;  > 0 and  &quot;Tol_pourcent&quot; &lt;= 100" symbol="2" key="{9c624dd7-04de-4258-9fe6-f2d4fe6e08a7}" label="Positif"/>
      <rule filter="&quot;ecart&quot; &lt; 0 and  &quot;Tol_pourcent&quot; > 100" symbol="3" key="{65509abb-8136-472e-96a3-bed660908f54}" label="Négatif - Hors tolérance"/>
      <rule filter=" &quot;ecart&quot;  &lt; 0 and  &quot;Tol_pourcent&quot; &lt;= 100" symbol="4" key="{b33d3dc1-ebd0-4563-b610-07d85455957b}" label="Négatif"/>
      <rule filter=" &quot;ecart&quot;  = 0" symbol="5" key="{0ddfd78c-b116-4ccd-9dcb-850c413eb0a2}" label="Pas d'écart"/>
    </rules>
    <symbols>
      <symbol alpha="1" type="fill" clip_to_extent="1" name="0" force_rhr="0">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
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
      <symbol alpha="1" type="fill" clip_to_extent="1" name="1" force_rhr="0">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="125,196,115,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
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
      <symbol alpha="1" type="fill" clip_to_extent="1" name="2" force_rhr="0">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="205,232,201,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
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
      <symbol alpha="1" type="fill" clip_to_extent="1" name="3" force_rhr="0">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,117,117,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
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
      <symbol alpha="1" type="fill" clip_to_extent="1" name="4" force_rhr="0">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,179,179,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
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
      <symbol alpha="1" type="fill" clip_to_extent="1" name="5" force_rhr="0">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,255,194,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
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
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings>
      <text-style fontItalic="0" fontCapitals="0" fontFamily="Cadastra" textColor="0,0,0,255" fontWordSpacing="0" useSubstitutions="0" fontUnderline="0" previewBkgrdColor="#ffffff" fontLetterSpacing="0" fieldName="ecart" textOpacity="1" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWeight="50" multilineHeight="1" fontSizeUnit="Point" fontStrikeout="0" namedStyle="Regular Condensed" blendMode="0" isExpression="0" fontSize="8.25">
        <text-buffer bufferColor="255,255,255,255" bufferSize="1" bufferDraw="0" bufferJoinStyle="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferNoFill="0" bufferBlendMode="0" bufferOpacity="1" bufferSizeUnits="MM"/>
        <background shapeType="0" shapeRotation="0" shapeRadiiX="0" shapeBorderColor="255,255,255,255" shapeFillColor="255,255,255,255" shapeOpacity="1" shapeSizeUnit="MM" shapeJoinStyle="64" shapeDraw="1" shapeSizeType="0" shapeSizeY="0" shapeOffsetUnit="MM" shapeOffsetY="0" shapeRadiiUnit="MM" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeBorderWidth="0" shapeBorderWidthUnit="MM" shapeSVGFile="" shapeOffsetX="0"/>
        <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowOffsetAngle="135" shadowRadius="1.5" shadowDraw="0" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowOpacity="0.7" shadowRadiusAlphaOnly="0" shadowRadiusUnit="MM" shadowOffsetDist="1" shadowScale="100" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0"/>
        <substitutions/>
      </text-style>
      <text-format wrapChar="" leftDirectionSymbol="&lt;" plussign="0" autoWrapLength="0" placeDirectionSymbol="0" formatNumbers="0" multilineAlign="0" decimals="3" useMaxLineLengthForAutoWrap="1" rightDirectionSymbol=">" addDirectionSymbol="0" reverseDirectionSymbol="0"/>
      <placement rotationAngle="0" geometryGenerator="" centroidWhole="0" offsetType="0" distMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" offsetUnits="MapUnit" maxCurvedCharAngleIn="20" geometryGeneratorEnabled="0" fitInPolygonOnly="0" dist="0" repeatDistance="0" xOffset="0" placement="1" priority="5" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" geometryGeneratorType="PointGeometry" maxCurvedCharAngleOut="-20" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" repeatDistanceUnits="MM" quadOffset="4" yOffset="0" centroidInside="0" placementFlags="0" distUnits="MM"/>
      <rendering scaleMax="10000" obstacleFactor="1" minFeatureSize="0" labelPerPart="0" mergeLines="0" displayAll="0" upsidedownLabels="0" drawLabels="1" obstacleType="0" limitNumLabels="0" fontMaxPixelSize="10000" zIndex="0" fontMinPixelSize="3" scaleMin="1" obstacle="1" scaleVisibility="1" fontLimitPixelSize="0" maxNumLabels="2000"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" type="QString" name="name"/>
          <Option type="Map" name="properties">
            <Option type="Map" name="Color">
              <Option value="true" type="bool" name="active"/>
              <Option value="CASE &#xa; WHEN Ecart  > 0 and  &quot;tol_pourcent&quot; > 100 THEN '0,0,255'&#xa; WHEN Ecart  > 0 and  &quot;tol_pourcent&quot;  &lt;= 100 THEN '0,0,255'&#xa; WHEN Ecart &lt; 0 and  &quot;tol_pourcent&quot; > 100 THEN '255,0,0'&#xa; WHEN Ecart &lt; 0 and  &quot;tol_pourcent&quot; &lt;= 100 THEN '255,0,0'&#xa; ELSE '0'&#xa;END" type="QString" name="expression"/>
              <Option value="3" type="int" name="type"/>
            </Option>
            <Option type="Map" name="Size">
              <Option value="true" type="bool" name="active"/>
              <Option value="CASE &#xa; WHEN Ecart  > 0 and  &quot;tol_pourcent&quot; > 100 THEN '15'&#xa; WHEN Ecart  > 0 and &quot;tol_pourcent&quot;  = 0 or  &quot;tol_pourcent&quot; &lt; 100 or  &quot;tol_pourcent&quot;  = 100 THEN '8'&#xa; WHEN Ecart &lt; 0 and  &quot;tol_pourcent&quot; > 100 THEN '15'&#xa; WHEN Ecart &lt; 0 and  &quot;tol_pourcent&quot; = 0 or  &quot;tol_pourcent&quot;  &lt; 100 THEN '8'&#xa; ELSE '0'&#xa;END" type="QString" name="expression"/>
              <Option value="3" type="int" name="type"/>
            </Option>
            <Option type="Map" name="Strikeout">
              <Option value="false" type="bool" name="active"/>
              <Option value="CASE &#xa; WHEN Ecart  > 0 and  &quot;%Tol&quot; > 100 THEN '1'&#xa; WHEN Ecart  > 0 and  &quot;%Tol&quot;  = 0 or  &quot;%Tol&quot; &lt; 100 or  &quot;%Tol&quot;  = 100 THEN '0'&#xa; WHEN Ecart &lt; 0 and  &quot;%Tol&quot; > 100 THEN '1'&#xa; WHEN Ecart &lt; 0 and  &quot;%Tol&quot; = 0 or  &quot;%Tol&quot;  &lt; 100 THEN '0'&#xa; ELSE '0'&#xa;END" type="QString" name="expression"/>
              <Option value="3" type="int" name="type"/>
            </Option>
            <Option type="Map" name="Underline">
              <Option value="true" type="bool" name="active"/>
              <Option value="CASE &#xa; WHEN Ecart  > 0 and  &quot;%Tol&quot; > 100 THEN '1'&#xa; WHEN Ecart  > 0 and  &quot;%Tol&quot;  = 0 or  &quot;%Tol&quot; &lt; 100 or  &quot;%Tol&quot;  = 100 THEN '0'&#xa; WHEN Ecart &lt; 0 and  &quot;%Tol&quot; > 100 THEN '1'&#xa; WHEN Ecart &lt; 0 and  &quot;%Tol&quot; = 0 or  &quot;%Tol&quot;  &lt; 100 THEN '0'&#xa; ELSE '0'&#xa;END" type="QString" name="expression"/>
              <Option value="3" type="int" name="type"/>
            </Option>
          </Option>
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
    <DiagramCategory penWidth="0" diagramOrientation="Up" barWidth="5" lineSizeScale="3x:0,0,0,0,0,0" opacity="1" minScaleDenominator="0" rotationOffset="270" scaleBasedVisibility="0" width="15" labelPlacementMethod="XHeight" penColor="#000000" penAlpha="255" sizeType="MM" sizeScale="3x:0,0,0,0,0,0" scaleDependency="Area" maxScaleDenominator="1e+08" enabled="0" lineSizeType="MM" height="15" minimumSize="0" backgroundColor="#ffffff" backgroundAlpha="255">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute label="" color="#000000" field=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings showAll="1" placement="1" linePlacementFlags="18" dist="0" obstacle="0" zIndex="0" priority="0">
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
    <field name="primaryindex">
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
    <field name="numero">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="egris_egrid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="validite">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="integralite">
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
    <field name="superficie_totale">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ecart">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tol">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tol_pourcent">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="justificatif">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" name="" field="primaryindex"/>
    <alias index="1" name="" field="identdn"/>
    <alias index="2" name="" field="numero"/>
    <alias index="3" name="" field="egris_egrid"/>
    <alias index="4" name="" field="validite"/>
    <alias index="5" name="" field="integralite"/>
    <alias index="6" name="" field="genre"/>
    <alias index="7" name="" field="superficie_totale"/>
    <alias index="8" name="" field="ecart"/>
    <alias index="9" name="" field="tol"/>
    <alias index="10" name="" field="tol_pourcent"/>
    <alias index="11" name="" field="justificatif"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" expression="" field="primaryindex"/>
    <default applyOnUpdate="0" expression="" field="identdn"/>
    <default applyOnUpdate="0" expression="" field="numero"/>
    <default applyOnUpdate="0" expression="" field="egris_egrid"/>
    <default applyOnUpdate="0" expression="" field="validite"/>
    <default applyOnUpdate="0" expression="" field="integralite"/>
    <default applyOnUpdate="0" expression="" field="genre"/>
    <default applyOnUpdate="0" expression="" field="superficie_totale"/>
    <default applyOnUpdate="0" expression="" field="ecart"/>
    <default applyOnUpdate="0" expression="" field="tol"/>
    <default applyOnUpdate="0" expression="" field="tol_pourcent"/>
    <default applyOnUpdate="0" expression="" field="justificatif"/>
  </defaults>
  <constraints>
    <constraint notnull_strength="1" exp_strength="0" constraints="3" field="primaryindex" unique_strength="1"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" field="identdn" unique_strength="0"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" field="numero" unique_strength="0"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" field="egris_egrid" unique_strength="0"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" field="validite" unique_strength="0"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" field="integralite" unique_strength="0"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" field="genre" unique_strength="0"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" field="superficie_totale" unique_strength="0"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" field="ecart" unique_strength="0"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" field="tol" unique_strength="0"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" field="tol_pourcent" unique_strength="0"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" field="justificatif" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="primaryindex"/>
    <constraint desc="" exp="" field="identdn"/>
    <constraint desc="" exp="" field="numero"/>
    <constraint desc="" exp="" field="egris_egrid"/>
    <constraint desc="" exp="" field="validite"/>
    <constraint desc="" exp="" field="integralite"/>
    <constraint desc="" exp="" field="genre"/>
    <constraint desc="" exp="" field="superficie_totale"/>
    <constraint desc="" exp="" field="ecart"/>
    <constraint desc="" exp="" field="tol"/>
    <constraint desc="" exp="" field="tol_pourcent"/>
    <constraint desc="" exp="" field="justificatif"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column type="field" name="primaryindex" hidden="0" width="-1"/>
      <column type="field" name="identdn" hidden="0" width="-1"/>
      <column type="field" name="numero" hidden="0" width="-1"/>
      <column type="field" name="egris_egrid" hidden="0" width="-1"/>
      <column type="field" name="validite" hidden="0" width="-1"/>
      <column type="field" name="integralite" hidden="0" width="-1"/>
      <column type="field" name="genre" hidden="0" width="-1"/>
      <column type="field" name="superficie_totale" hidden="0" width="-1"/>
      <column type="field" name="ecart" hidden="0" width="-1"/>
      <column type="field" name="tol" hidden="0" width="-1"/>
      <column type="field" name="justificatif" hidden="0" width="-1"/>
      <column type="actions" hidden="1" width="-1"/>
      <column type="field" name="tol_pourcent" hidden="0" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1">.</editform>
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
    <field editable="1" name="%tol"/>
    <field editable="1" name="ecart"/>
    <field editable="1" name="egris_egrid"/>
    <field editable="1" name="genre"/>
    <field editable="1" name="identdn"/>
    <field editable="1" name="integralite"/>
    <field editable="1" name="justificatif"/>
    <field editable="1" name="numero"/>
    <field editable="1" name="primaryindex"/>
    <field editable="1" name="superficie_totale"/>
    <field editable="1" name="tol"/>
    <field editable="1" name="tol_pourcent"/>
    <field editable="1" name="validite"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="%tol"/>
    <field labelOnTop="0" name="ecart"/>
    <field labelOnTop="0" name="egris_egrid"/>
    <field labelOnTop="0" name="genre"/>
    <field labelOnTop="0" name="identdn"/>
    <field labelOnTop="0" name="integralite"/>
    <field labelOnTop="0" name="justificatif"/>
    <field labelOnTop="0" name="numero"/>
    <field labelOnTop="0" name="primaryindex"/>
    <field labelOnTop="0" name="superficie_totale"/>
    <field labelOnTop="0" name="tol"/>
    <field labelOnTop="0" name="tol_pourcent"/>
    <field labelOnTop="0" name="validite"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>identdn</previewExpression>
  <mapTip>OGC_FID</mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
