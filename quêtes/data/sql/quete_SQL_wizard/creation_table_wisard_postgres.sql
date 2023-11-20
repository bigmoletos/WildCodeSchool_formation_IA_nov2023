
SELECT datname AS nom_base_de_donnees,
       pg_encoding_to_char(encoding) AS encodage
FROM pg_database
WHERE datname = 'wild_db_quest';
DROP TABLE IF EXISTS wizard;

CREATE TABLE wizard (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    birthday DATE NOT NULL,
    birth_place VARCHAR(255),
    biography TEXT,
    is_muggle BOOLEAN NOT NULL
);

INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('harry', 'potter', '1980-07-31', 'london', '', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('hermione', 'granger', '1979-09-19', '', 'Friend of Harry Potter', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('lily', 'potter', '1960-01-30', '', 'mother of Harry Potter', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('ron', 'weasley', '1980-03-01', '', 'Best friend of Harry', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('ginny', 'weasley', '1981-08-11', '', 'Sister of Ron and girlfriend of Harry', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('fred', 'weasley', '1978-04-01', '', '', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('george', 'weasley', '1978-04-01', '', '', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('arthur', 'weasley', '1950-02-06', '', '', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('molly', 'weasley', '1949-01-01', '', '', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('drago', 'malefoy', '1980-06-05', '', '', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('albus', 'dumbledore', '1881-07-01', '', '', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('severus', 'rogue', '1960-01-09', '', '', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('tom', 'jédusor', '1926-12-31', '', 'Celui-Dont-On-Ne-Doit-Pas-Prononcer-Le-Nom alias Voldermort', '0');
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('dudley', 'dursley', '1980-06-23', '', 'Cousin d''Harry', '1');
