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
select CONCAT(firstname, ' ', lastname) AS fullname
from player p 
inner join wizard w  using(id) 
where enrollment_date between '1995-01-01' and '1998-01-01'
and role='chaser'
;




-- 4 Affiche le nombre de joueurs par rôle et par équipe


-- 5 Affiche, pour l’équipe 'Gryffindor', les nom, prénom et le rôle des joueurs dont le rôle est 'chaser'
