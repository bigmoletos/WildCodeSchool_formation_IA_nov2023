/*quete_SQL3_manipulation des données*/
-- Supprime la table 'school' si elle existe déjà
DROP TABLE IF EXISTS school;

-- Crée la table 'school'
CREATE TABLE school (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(255),
    capacity INT
);

-- Insère des données dans la table 'school'
INSERT INTO school (name, country, capacity)
VALUES
('Beauxbatons Academy of Magic', 'France', 550),
('Castelobruxo', 'Brazil', 380),
('Durmstrang Institute', 'Norway', 570),
('Hogwarts School of Witchcraft and Wizardry', 'United Kingdom', 450),
('Ilvermorny School of Witchcraft and Wizardry', 'USA', 300),
('Koldovstoretz', 'Russia', 125),
('Mahoutokoro School of Magic', 'Japan', 800),
('Uagadou School of Magic', 'Uganda', 350);

-- Met à jour la colonne 'country' de la table 'school' pour certaines lignes
--“Durmstrang Institute” est en réalité en Suède (Sweden), modifie son pays.
UPDATE school SET  country = 'Sweden' WHERE    name LIKE 'Durmstrang%';

-- Met à jour la colonne 'capacity' de la table 'school' pour certaines lignes
--“Mahoutokoro School of Magic” passe à une capacité de 700
UPDATE school SET  capacity = 700  WHERE  name LIKE 'Mahoutokoro%';

--Supprime en une seule requête toutes les écoles comportant “Magic” dans leur nom (il y en a 3). Tu peux t’aider du mot clé LIKE.
DELETE FROM school WHERE   name LIKE '%Magic%';

-- Sélectionne toutes les données de la table 'school'
SELECT * FROM  school ORDER BY capacity;
