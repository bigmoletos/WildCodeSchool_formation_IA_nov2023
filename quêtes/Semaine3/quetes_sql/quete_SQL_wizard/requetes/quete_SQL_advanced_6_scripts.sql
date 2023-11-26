-- Renvoie les noms des équipes et le nombre de joueurs dans chaque équipe, 
-- tous triés par le nombre de joueurs dans chaque équipe, du plus élevé au plus faible.

-- Retourne les noms des équipes complètes uniquement (de 14 joueurs ou plus,
--  soit un minimum de 7 joueurs et 7 joueurs remplaçants), triées par ordre alphabétique.

-- L’entraîneur de Gryffondor est superstitieux, sa journée préférée est le lundi. 
-- Retournez la liste des joueurs de son équipe inscrits un lundi 
-- (il veut qu'ils jouent en premier) et triez les résultats par date d'inscription.
use tournament;
select *from team;
select *from player;
select *from wizard;
-- Renvoie les noms des équipes et le nombre de joueurs dans chaque équipe, 
-- tous triés par le nombre de joueurs dans chaque équipe, du plus élevé au plus faible.
SELECT 
    name, COUNT(p.team_id) AS nb_player
FROM
    player p
        JOIN
    team t ON t.id = team_id
GROUP BY p.team_id
ORDER BY nb_player desc;
-- Retourne les noms des équipes complètes uniquement (de 14 joueurs ou plus,
--  soit un minimum de 7 joueurs et 7 joueurs remplaçants), triées par ordre alphabétique.
SELECT 
    name, COUNT(p.team_id) AS nb_player
FROM
    player p
        JOIN
    team t ON t.id = team_id
GROUP BY p.team_id
having nb_player >=14
ORDER BY name ;

-- L’entraîneur de Gryffondor est superstitieux, sa journée préférée est le lundi. 
-- Retournez la liste des joueurs de son équipe inscrits un lundi 
-- (il veut qu'ils jouent en premier) et triez les résultats par date d'inscription.

SELECT 
 name, w.lastname , w.firstname, DAYOFWEEK(p.enrollment_date) AS jourSemaine
FROM
    player p
        JOIN
    team t ON t.id = team_id
        JOIN
    wizard w ON w.id = wizard_id
    
where name='Gryffindor' and DAYOFWEEK(enrollment_date) = 2
ORDER BY lastname, firstname;

SELECT 
 team_id, wizard_id,name, firstname,lastname, role, DAYOFWEEK(enrollment_date) AS 'jourSemaine'
FROM
    player p
        JOIN
    team t ON t.id = team_id
        JOIN
    wizard w ON w.id = wizard_id
--    where  jourSemaine = 2
  where name='Gryffindor'  and DAYOFWEEK(enrollment_date) = 2
    order by  jourSemaine, name;
