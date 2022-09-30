<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyLocal="1" version="3.4.4-Madeira" readOnly="0" minScale="1e+08" simplifyDrawingTol="1" simplifyMaxScale="1" labelsEnabled="0" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1" maxScale="0" simplifyAlgorithm="0" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" symbollevels="0" type="singleSymbol" enableorderby="0">
    <symbols>
      <symbol alpha="1" name="0" type="fill" clip_to_extent="1" force_rhr="0">
        <layer locked="0" enabled="1" class="SimpleFill" pass="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="215,255,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1.46" k="outline_width"/>
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
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory rotationOffset="270" labelPlacementMethod="XHeight" maxScaleDenominator="1e+08" minScaleDenominator="0" diagramOrientation="Up" penColor="#000000" penWidth="0" backgroundAlpha="255" opacity="1" width="15" sizeType="MM" backgroundColor="#ffffff" lineSizeType="MM" height="15" scaleDependency="Area" penAlpha="255" minimumSize="0" lineSizeScale="3x:0,0,0,0,0,0" barWidth="5" scaleBasedVisibility="0" sizeScale="3x:0,0,0,0,0,0" enabled="0">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" dist="0" placement="1" zIndex="0" priority="0" showAll="1" linePlacementFlags="18">
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
    <field name="tolerancesurface">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tolerancelargeur">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nomcomparaison">
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
    <alias name="" index="1" field="tolerancesurface"/>
    <alias name="" index="2" field="tolerancelargeur"/>
    <alias name="" index="3" field="nomcomparaison"/>
    <alias name="" index="4" field="observation"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" field="OGC_FID" applyOnUpdate="0"/>
    <default expression="" field="tolerancesurface" applyOnUpdate="0"/>
    <default expression="" field="tolerancelargeur" applyOnUpdate="0"/>
    <default expression="" field="nomcomparaison" applyOnUpdate="0"/>
    <default expression="" field="observation" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" constraints="3" notnull_strength="1" unique_strength="1" field="OGC_FID"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="tolerancesurface"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="tolerancelargeur"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="nomcomparaison"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="observation"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="OGC_FID"/>
    <constraint desc="" exp="" field="tolerancesurface"/>
    <constraint desc="" exp="" field="tolerancelargeur"/>
    <constraint desc="" exp="" field="nomcomparaison"/>
    <constraint desc="" exp="" field="observation"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column name="OGC_FID" type="field" hidden="0" width="-1"/>
      <column name="tolerancesurface" type="field" hidden="0" width="-1"/>
      <column name="tolerancelargeur" type="field" hidden="0" width="-1"/>
      <column name="nomcomparaison" type="field" hidden="0" width="-1"/>
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
    <field name="OGC_FID" editable="1"/>
    <field name="nomcomparaison" editable="1"/>
    <field name="observation" editable="1"/>
    <field name="tolerancelargeur" editable="1"/>
    <field name="tolerancesurface" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="OGC_FID"/>
    <field labelOnTop="0" name="nomcomparaison"/>
    <field labelOnTop="0" name="observation"/>
    <field labelOnTop="0" name="tolerancelargeur"/>
    <field labelOnTop="0" name="tolerancesurface"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
