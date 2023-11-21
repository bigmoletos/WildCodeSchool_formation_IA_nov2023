DROP TABLE IF EXISTS school;
CREATE TABLE school (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    capacity INT
);

INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('harry', 'potter', '1980-07-31', 'london', '', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('hermione', 'granger', '1979-09-19', '', 'Friend of Harry Potter', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('lily', 'potter', '1960-01-30', '', 'mother of Harry Potter', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('ron', 'weasley', '1980-03-01', '', 'Best friend of Harry', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('ginny', 'weasley', '1981-08-11', '', 'Sister of Ron and girlfriend of Harry', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('fred', 'weasley', '1978-04-01', '', '', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('george', 'weasley', '1978-04-01', '', '', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('arthur', 'weasley', '1950-02-06', '', '', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('molly', 'weasley', ' 1949-01-01', '', '', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('drago', 'malefoy', '1980-06-05', '', '', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('albus', 'dumbledore', '1881-07-01', '', '', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('severus', 'rogue', '1960-01-09', '', '', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('tom', 'jÃ©dusor', '1926-12-31', '', 'Celui-Dont-On-Ne-Doit-Pas-Prononcer-Le-Nom alias Voldermort', false);
INSERT INTO wizard (firstname, lastname, birthday, birth_place, biography, is_muggle) VALUES ('dudley', 'dursley', '1980-06-23', '', 'Cousin d''Harry', true);
