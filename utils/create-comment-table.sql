CREATE TABLE 'justificatif_nogeometry' (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session TEXT NOT NULL,
  layer TEXT NOT NULL,
  topic TEXT NOT NULL,
  statut TEXT NOT NULL,
  texte TEXT NOT NULL
)

CREATE TABLE 'justificatif_point' (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  geometry POINT,
  session TEXT NOT NULL,
  layer TEXT NOT NULL,
  topic TEXT NOT NULL,
  statut TEXT NOT NULL,
  texte TEXT NOT NULL
)

CREATE TABLE 'justificatif_line' (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  geometry COMPOUNDCURVE,
  session TEXT NOT NULL,
  layer TEXT NOT NULL,
  topic TEXT NOT NULL,
  statut TEXT NOT NULL,
  texte TEXT NOT NULL
)

CREATE TABLE 'justificatif_polygon' (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  geometry CURVEPOLYGON,
  session TEXT NOT NULL,
  layer TEXT NOT NULL,
  topic TEXT NOT NULL,
  statut TEXT NOT NULL,
  texte TEXT NOT NULL
)

INSERT INTO gpkg_contents (table_name, data_type) values ('justificatif_nogeometry','attributes');
INSERT INTO gpkg_contents (table_name, data_type) values ('justificatif_point','features');
INSERT INTO gpkg_geometry_columns (table_name, column_name, geometry_type_name, srs_id, z, m) VALUES ('justificatif_point', 'geometry', 'POINT', 2056, 0, 0);
INSERT INTO gpkg_contents (table_name, data_type) values ('justificatif_line','features');
INSERT INTO gpkg_geometry_columns (table_name, column_name, geometry_type_name, srs_id, z, m) VALUES ('justificatif_line', 'geometry', 'COMPOUNDCURVE', 2056, 0, 0);
INSERT INTO gpkg_contents (table_name, data_type) values ('justificatif_polygon','features');
INSERT INTO gpkg_geometry_columns (table_name, column_name, geometry_type_name, srs_id, z, m) VALUES ('justificatif_polygon', 'geometry', 'CURVEPOLYGON', 2056, 0, 0);



-- insert example
insert into commentaires (
  geometry,
  geometry_type,
  session,
  topic,
  statut,
  texte
) values (
  st_geomfromtext('Point(2541375 1151076)'),
  'POINT',
  'session',
  'topic',
  'valide',
  'mon commentaire');

insert into commentaires (
  geometry,
  geometry_type,
  session,
  topic,
  statut,
  texte
) values (
  st_geomfromtext('LineString(2541370 1151070, 2541379 1151071)'),
  'LINESTRING',
  'session 2',
  'topic 2',
  'valide 2',
  'mon commentaire 2');
