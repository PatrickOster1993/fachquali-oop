-- Tabelle: artists
CREATE TABLE artists (
  artist_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

-- Tabelle: albums
CREATE TABLE albums (
  album_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  artist_id INT,
  release_year INT,
  FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

-- Tabelle: songs
CREATE TABLE songs (
  song_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  album_id INT,
  duration_seconds INT NOT NULL,
  FOREIGN KEY (album_id) REFERENCES albums(album_id)
);

-- Beispiel-Daten
INSERT INTO artists (name) VALUES
  ('The Beatles'),
  ('Adele'),
  ('Ed Sheeran'),
  ('Imagine Dragons'),
  ('Unknown Artist');

INSERT INTO albums (title, artist_id, release_year) VALUES
  ('Abbey Road', 1, 1969),  -- Zu The Beatles
  ('21', 2, 2011),  -- Zu Adele
  ('Divide', 3, 2017),  -- Zu Ed Sheeran
  ('Evolve', 4, 2017),  -- Zu Imagine Dragons
  ('Untitled Album', NULL, 2020);  -- Kein Künstler zugeordnet

INSERT INTO songs (title, album_id, duration_seconds) VALUES
  ('Come Together', 1, 259),
  ('Here Comes the Sun', 1, 186),
  ('Someone Like You', 2, 285),
  ('Shape of You', 3, 263),
  ('Believer', 4, 204),
  ('Unknown Song', 5, 300); -- Song zu einem Album ohne Künstler
  
  -- Verschiedene Arten von JOINs:
  
  -- (INNER) JOIN: gibt nur Datensätze zurück, sofern es eine Übereinstimmung in beiden Tables gibt!
  select ar.name as Kuenstler, al.title as Album
  from artists ar
  INNER JOIN albums al on al.artist_id = ar.artist_id;
  
  -- LEFT JOIN: gibt alle Datensätze aus der LINKEN Table zurück!
  -- und wenn es eine Übereinstimmung mit der rechten Tabelle gibt, werden auch diese Datensätze ausgegeben!
  select ar.name as Kuenstler, al.title as Album
  from artists ar
  LEFT JOIN albums al on al.artist_id = ar.artist_id;
  
  -- RIGHT JOIN: gibt alle Datensätze aus der RECHTE Table zurück!
  -- und wenn es eine Übereinstimmung mit der linken Tabelle gibt, werden auch diese Datensätze ausgegeben!
  select ar.name as Kuenstler, al.title as Album
  from artists ar
  RIGHT JOIN albums al on al.artist_id = ar.artist_id;
  
  -- Einfache Fallunterscheidungen:
  
  -- 1. IF
  select title as Titel, IF(duration_seconds > 200, 'lang', 'kurz') as Songlaenge
  from songs;
  
  -- 2. NULLIF --> Falls artist_id gegeben, wird diese zurückgeliefert... andernfalls NULL!
  select title as Albumname, NULLIF(artist_id, NULL) as id_check
  from albums;
  
  -- 3. IFNULL --> Falls artist_id gegeben, wird diese zurückgeliefert... andernfalls 0!
  select title as Albumname, IFNULL(artist_id, 0) as id_check
  from albums;