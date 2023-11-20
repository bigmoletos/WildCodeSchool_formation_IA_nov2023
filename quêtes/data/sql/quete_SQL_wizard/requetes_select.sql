-- Affiche les prénoms et noms des sorciers qui se sont inscrits comme joueurs entre les années 1995 et 1998 (enrollment_date).
SELECT * FROM wizard WHERE birthday BETWEEN '1995-01-01' AND '1998-01-01';

--selection noms commencant par H
SELECT firstname FROM wizard WHERE firstname LIKE 'H%';

-- selection du prenom
/*
SELECT firstname, lastname
FROM wizard
WHERE lastname = 'potter'
ORDER BY firstname;
ADMIN

--selection aniversaires
SELECT firstname, lastname, birthday
FROM wizard
ORDER BY birthday
LIMIT 1;
*/

--selection nom
SELECT firstname FROM wizard

/*1 Affiche les prénoms et noms des sorciers (wizards) qui se sont inscrits comme joueurs entre les années 1995 et 1998 (enrollment_date) et qui ont pour rôle 'keeper'*/

/*2 Affiche les prénoms et noms des sorciers (wizards) qui se sont inscrits comme joueurs entre les années 1995 et 1998 (enrollment_date) et qui ont pour rôle 'keeper'*/



/*3 Affiche les prénoms, noms et rôles des sorciers (wizards) qui se sont inscrits comme joueurs entre les années 1995 et 1998 (enrollment_date) et qui ont pour rôle ‘chaser’
Indice : tu auras besoin d’une jointure*/

/*4 Affiche le nombre de joueurs par rôle et par équipe
5 Affiche, pour l’équipe 'Gryffindor', les nom, prénom et le rôle des joueurs dont le rôle est 'chaser'*/


