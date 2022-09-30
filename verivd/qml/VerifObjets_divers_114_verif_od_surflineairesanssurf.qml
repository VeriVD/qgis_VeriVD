<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" version="3.8.2-Zanzibar" simplifyDrawingTol="1" simplifyMaxScale="1" minScale="1e+08" styleCategories="AllStyleCategories" simplifyDrawingHints="1" simplifyAlgorithm="0" hasScaleBasedVisibilityFlag="0" labelsEnabled="0" simplifyLocal="1" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" enableorderby="0" type="singleSymbol" symbollevels="0">
    <symbols>
      <symbol name="0" type="line" clip_to_extent="1" alpha="1" force_rhr="0">
        <layer pass="0" locked="0" class="SimpleLine" enabled="1">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,128,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="2"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
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
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory minScaleDenominator="0" penWidth="0" minimumSize="0" enabled="0" maxScaleDenominator="1e+08" sizeScale="3x:0,0,0,0,0,0" width="15" scaleBasedVisibility="0" labelPlacementMethod="XHeight" height="15" backgroundAlpha="255" penColor="#000000" rotationOffset="270" lineSizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" lineSizeType="MM" penAlpha="255" barWidth="5" scaleDependency="Area" sizeType="MM" opacity="1" diagramOrientation="Up">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" linePlacementFlags="18" placement="2" showAll="1" dist="0" zIndex="0" obstacle="0">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
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
    <field name="element_lineaire_de">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ufid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="fid_od">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="origine">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="qualite">
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
    <alias index="0" name="" field="OGC_FID"/>
    <alias index="1" name="" field="xtf_id"/>
    <alias index="2" name="" field="element_lineaire_de"/>
    <alias index="3" name="" field="ufid"/>
    <alias index="4" name="" field="fid_od"/>
    <alias index="5" name="" field="origine"/>
    <alias index="6" name="" field="qualite"/>
    <alias index="7" name="" field="genre"/>
    <alias index="8" name="" field="observation"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" expression="" field="OGC_FID"/>
    <default applyOnUpdate="0" expression="" field="xtf_id"/>
    <default applyOnUpdate="0" expression="" field="element_lineaire_de"/>
    <default applyOnUpdate="0" expression="" field="ufid"/>
    <default applyOnUpdate="0" expression="" field="fid_od"/>
    <default applyOnUpdate="0" expression="" field="origine"/>
    <default applyOnUpdate="0" expression="" field="qualite"/>
    <default applyOnUpdate="0" expression="" field="genre"/>
    <default applyOnUpdate="0" expression="" field="observation"/>
  </defaults>
  <constraints>
    <constraint constraints="3" unique_strength="1" notnull_strength="1" field="OGC_FID" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="xtf_id" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="element_lineaire_de" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="ufid" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="fid_od" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="origine" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="qualite" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="genre" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="observation" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="OGC_FID" desc=""/>
    <constraint exp="" field="xtf_id" desc=""/>
    <constraint exp="" field="element_lineaire_de" desc=""/>
    <constraint exp="" field="ufid" desc=""/>
    <constraint exp="" field="fid_od" desc=""/>
    <constraint exp="" field="origine" desc=""/>
    <constraint exp="" field="qualite" desc=""/>
    <constraint exp="" field="genre" desc=""/>
    <constraint exp="" field="observation" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column hidden="0" name="OGC_FID" width="-1" type="field"/>
      <column hidden="0" name="xtf_id" width="-1" type="field"/>
      <column hidden="0" name="element_lineaire_de" width="-1" type="field"/>
      <column hidden="0" name="ufid" width="-1" type="field"/>
      <column hidden="0" name="fid_od" width="-1" type="field"/>
      <column hidden="0" name="origine" width="-1" type="field"/>
      <column hidden="0" name="qualite" width="-1" type="field"/>
      <column hidden="0" name="genre" width="-1" type="field"/>
      <column hidden="0" name="observation" width="-1" type="field"/>
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
    <field name="OGC_FID" editable="1"/>
    <field name="element_lineaire_de" editable="1"/>
    <field name="fid_od" editable="1"/>
    <field name="genre" editable="1"/>
    <field name="observation" editable="1"/>
    <field name="origine" editable="1"/>
    <field name="qualite" editable="1"/>
    <field name="ufid" editable="1"/>
    <field name="xtf_id" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="OGC_FID" labelOnTop="0"/>
    <field name="element_lineaire_de" labelOnTop="0"/>
    <field name="fid_od" labelOnTop="0"/>
    <field name="genre" labelOnTop="0"/>
    <field name="observation" labelOnTop="0"/>
    <field name="origine" labelOnTop="0"/>
    <field name="qualite" labelOnTop="0"/>
    <field name="ufid" labelOnTop="0"/>
    <field name="xtf_id" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>OGC_FID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
