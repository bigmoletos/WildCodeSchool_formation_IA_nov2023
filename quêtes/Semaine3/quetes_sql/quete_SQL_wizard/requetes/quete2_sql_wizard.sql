/*
Récupère tous les champs pour les sorciers nés entre 1975 et 1985
Le prénom uniquement des sorciers dont le prénom commence par la lettre ‘H’
Les prénom et nom de tous les membres de la famille ‘Potter’, classés par ordre de prénom
Le prénom, nom et date de naissance du plus vieux sorcier (doit fonctionner quelque soit le contenu de la table)
*/

USE `wild_db_quest`;

SELECT 
    *
FROM
    wizard
WHERE
    birthday BETWEEN '1975-01-01' AND '1985-01-01';

SELECT 
    firstname
FROM
    wizard
WHERE
    firstname LIKE 'H%';

SELECT 
    firstname, lastname
FROM
    wizard
WHERE
    lastname = 'potter'
ORDER BY firstname;

SELECT 
    firstname, lastname, birthday
FROM
    wizard
ORDER BY birthday
LIMIT 1;

