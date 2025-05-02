-- Tabellen
CREATE TABLE artists (
  artist_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE albums (
  album_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  artist_id INT,
  release_year INT,
  FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

-- Infos zu FOREIGN KEY:
---- es gibt 3 wichtige Schlüsselwörter, mit denen Sie das Verhalten beim Löschen oder Ändern 
---- der Tabelle vorgeben. Oder anders ausgedrückt: Was soll in der verknüpften Tabelle vor sich gehen,
---- wenn in der anderen Tabelle etwas geändert (update) oder gelöscht (delete) wird!

---- RESTRICT: Verhindert Ändern oder Löschen von Daten in übergeordneter Tabelle,
---- wenn es abhängige Datensätze in referenzierter Tabelle gibt!

---- CASCADE: Wenn in übergeordneter Tabelle etwas geändert oder gelöscht wird,
---- werden auch alle abhängigen Datensätze in referenziert Tabelle mitgelöscht / geändert!

---- SET NULL: Wenn in übergeordneter Tabelle etwas geändert oder gelöscht wird,
---- werden auch alle abhängigen Datensätze in referenziert Tabelle die verknüpften Daten auf NULL gesetzt!

CREATE TABLE songs (
  song_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  album_id INT,
  duration_seconds INT NOT NULL
);

-- Beispiel-Daten
INSERT INTO artists (name) VALUES
  ('The Beatles'),
  ('Adele'),
  ('Ed Sheeran'),
  ('Imagine Dragons');

INSERT INTO albums (title, artist_id, release_year) VALUES
  ('Abbey Road', 1, 1969),
  ('21', 2, 2011),
  ('Divide', 3, 2017),
  ('Evolve', 4, 2017);

INSERT INTO songs (title, album_id, duration_seconds) VALUES
  ('Come Together', 1, 259),
  ('Here Comes the Sun', 1, 186),
  ('Someone Like You', 2, 285),
  ('Shape of You', 3, 263),
  ('Believer', 4, 204);

-- Aufgabe 1:
-- Gib alle Künstlernamen aus, die mindestens ein Album veröffentlicht haben.

---- Lösung über Subquery:
select name from artists
where artist_id in (
  	select artist_id from albums
  );

---- Lösung über JOIN:
select a.name
from artists a
join albums al on a.artist_id = al.artist_id;

-- Aufgabe 2:
-- Finde den Titel des Songs, der die längste Dauer hat.
select title from songs
order by duration_seconds desc
limit 1;

-- Aufgabe 3:
-- Zeige alle Songs an, die in einem Album von Adele enthalten sind.

---- Lösung über Subquery
select title from songs
where album_id in (
  	select album_id from albums
  	where artist_id = (
      	select artist_id from artists
      	where name = 'Adele'
      )
  );

---- Lösung über JOIN
select s.title from songs s
join albums al on s.album_id = al.album_id
join artists a on a.artist_id = al.artist_id
where a.name = 'Adele';

-- Aufgabe 4:
-- Finde den Künstlernamen und den Titel der Songs, die mehr als 250 Sekunden dauern.
-- (Verwende einen JOIN zwischen songs und artists.)
select a.name as Kuenstler, s.title as Titel
from songs s
join albums al on al.album_id = s.album_id
join artists a on a.artist_id = al.artist_id
where s.duration_seconds > 250;

-- Aufgabe 5:
-- Berechne die durchschnittliche Dauer der Songs in jedem Album.
-- 1 x über Subquery und 1 x über JOIN

select a.title as Album_Titel, 
(
  select AVG(s.duration_seconds) 
  from songs s
  where s.album_id = a.album_id
) as Durchschnittsdauer
from albums a;

select a.title as Album_Titel, AVG(s.duration_seconds) as Durchschnittsdauer
from albums a
join songs s on a.album_id = s.album_id
group by a.album_id;

-- Aufgabe 6:
-- Zeige alle Alben an, die nach 2010 veröffentlicht wurden.

select title
from albums
where release_year > 2010;

-- Aufgabe 7:
-- Berechne die Gesamtdauer aller Songs eines bestimmten Albums (Beispiel: Abbey Road)
-- (Verwende Subqueries)

SELECT 
    SUM(duration_seconds) AS Gesamtdauer
FROM 
    songs
WHERE 
    album_id = (SELECT album_id FROM albums
                WHERE title = 'Abbey Road');

-- Aufgabe 8:
-- Erstelle eine Stored Procedure namens get_songs_by_album,
-- die alle Songs eines bestimmten Albums zurückgibt.
-- Übergabeparameter: album_name VARCHAR(100).
-- 
-- Hinweis: Statt Subqueries oder Joins zu verwenden, kannst du hier
-- mit Variablen arbeiten, um das gewünschte Ergebnis zu erzielen.
-- Der Vorteil einer Stored Procedure ist, dass du 
-- einzelne Abfrageergebnisse in einer Variable zwischenspeichern kannst, 
-- und dann mit dieser Variable einfach in einer neuen Query weiterarbeiten kannst.
-- Zusatzschritt: Aufgabe 7 in procedure integrieren!
DELIMITER //
create procedure get_songs_by_album(in album_name VARCHAR(100))
begin
		
   	 declare temp_album_id INT;
     declare gesamtdauer INT;
     
     select album_id into temp_album_id
     from albums
     where title = album_name;
     
     select SUM(duration_seconds) into gesamtdauer
     from songs
     where album_id = temp_album_id;
     
     select title as Song, duration_seconds as Dauer, ((duration_seconds / gesamtdauer) * 100) as Anteil_an_Gesamtdauer
     from songs
     where album_id = temp_album_id;
    
end //
DELIMITER ;

call get_songs_by_album('Abbey Road');
call get_songs_by_album('Divide');