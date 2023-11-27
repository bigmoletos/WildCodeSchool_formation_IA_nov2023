-- 1 Affiche les prénoms et noms des sorciers qui se sont inscrits comme joueurs entre les années 1995 et 1998 (enrollment_date).
select CONCAT(firstname, ' ', lastname) AS fullname
from player p 
inner join wizard w  using(id) 
where enrollment_date between '1995-01-01' and '1998-01-01';

-- 2 Affiche les prénoms et noms des sorciers (wizards) qui se sont inscrits comme joueurs entre les années 1995 et 1998 (enrollment_date) et qui ont pour rôle 'keeper'
select CONCAT(firstname, ' ', lastname) AS fullname
from player p 
inner join wizard w  using(id) 
where enrollment_date between '1995-01-01' and '1998-01-01'
and role='keeper'
;


-- 3 Affiche les prénoms, noms et rôles des sorciers (wizards) qui se sont inscrits comme joueurs entre les années 1995 et 1998 (enrollment_date) et qui ont pour rôle ‘chaser’
-- Indice : tu auras besoin d’une jointure
select CONCAT(firstname, ' ', lastname) AS fullname, role
from player p 
inner join wizard w  using(id) 
where enrollment_date between '1995-01-01' and '1998-01-01'
and role='chaser'
;

-- 4 Affiche le nombre de joueurs par rôle et par équipe
-- création vue nombre de joueur par role
USE wild_db_quest;
DROP VIEW IF EXISTS joueurs_par_role;
CREATE VIEW joueurs_par_role AS
SELECT
COUNT(w.lastname) AS 'nombre de joueurs',
p.role
FROM player p 
INNER JOIN wizard w ON p.id = w.id
GROUP BY p.role;
-- utilisation de la vue
SELECT
t.name AS 'equipe',
Count(j.`nombre de joueurs`) AS 'nombre total de joueurs'
FROM joueurs_par_role j
INNER JOIN player p ON j.role = p.role
INNER JOIN team t ON p.team_id = t.id
GROUP BY t.name;

-- 5 Affiche, pour l’équipe 'Gryffindor', les nom, prénom et le rôle des joueurs dont le rôle est 'chaser'

SELECT 
t.name AS 'equipe',
w.firstname AS 'Prénom', 
w.lastname AS 'Nom', 
p.role AS 'Rôle'
FROM player p 
inner join wizard w  using(id) 
INNER JOIN team t ON p.team_id = t.id
WHERE t.name = 'Gryffindor' AND p.role = 'chaser';

-- autre solution
/*USE wild_db_quest;
DROP VIEW IF EXISTS Gryffindor_Chasers;
CREATE VIEW Gryffindor_Chasers AS
SELECT firstname, lastname, role
FROM player p
WHERE name = 'Gryffindor' AND role = 'chaser';

SELECT * FROM Gryffindor_Chasers;*/


