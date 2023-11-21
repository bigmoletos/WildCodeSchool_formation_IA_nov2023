-- Affiche les prénoms et noms des sorciers qui se sont inscrits comme joueurs entre les années 1995 et 1998 (enrollment_date).
SELECT * FROM wizard WHERE birthday BETWEEN '1995-01-01' AND '1998-01-01';

--selection noms commencant par H
SELECT firstname FROM wizard WHERE firstname LIKE 'h%';

-- selection du prenom
SELECT firstname, lastname FROM wizard WHERE lastname = 'potter' ORDER BY  firstname;

--selection aniversaires
SELECT firstname, lastname, birthday FROM wizard ORDER BY birthday LIMIT 1;

--insertion des données dans school
INSERT INTO school (name, country, capacity)
VALUES
('Beauxbatons Academy of Magic', 'France', 550),
('Castelobruxo', 'Brazil', 380),
('Durmstrang Institute', 'Norway', 570),
('Hogwarts School of Witchcraft and Wizardry', 'United Kingdom', 450),
('Ilvermorny School of Witchcraft and Wizardry', 'USA', 300),
('Koldovstoretz', 'Russia', 125),
('Mahoutokoro School of Magic', 'Japan', 800),
('Uagadou School of Magic', 'Uganda', 350),
('Bossancourt tradition', 'France', 312),
('Tocapuria', 'Brazil', 67),
('Kiopler', 'Norway', 765),
('OldStudent School of Witchcraft and Wizardry', 'United Kingdom', 90),
('Wit School of Witchcraft and Wizardry', 'USA', 543),
('Loudmila', 'Russia', 98),
('Yamathi School of Magic', 'Japan', 76),
('Tambouktou School of Magic', 'Uganda', 765);

/*1 Affiche les prénoms et noms des sorciers (wizards) qui se sont inscrits comme joueurs entre les années 1995 et 1998 (enrollment_date) et qui ont pour rôle 'keeper'*/


/*2 Affiche les prénoms et noms des sorciers (wizards) qui se sont inscrits comme joueurs entre les années 1995 et 1998 (enrollment_date) et qui ont pour rôle 'keeper'*/



/*3 Affiche les prénoms, noms et rôles des sorciers (wizards) qui se sont inscrits comme joueurs entre les années 1995 et 1998 (enrollment_date) et qui ont pour rôle ‘chaser’
Indice : tu auras besoin d’une jointure*/

/*4 Affiche le nombre de joueurs par rôle et par équipe
5 Affiche, pour l’équipe 'Gryffindor', les nom, prénom et le rôle des joueurs dont le rôle est 'chaser'*/


