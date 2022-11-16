CREATE TABLE 'justficatif' (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  geometry GEOMETRYCOLLECTION,
  geometry_type TEXT,
  session TEXT NOT NULL,
  topic TEXT NOT NULL,
  statut TEXT NOT NULL,
  texte TEXT NOT NULL
)

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
