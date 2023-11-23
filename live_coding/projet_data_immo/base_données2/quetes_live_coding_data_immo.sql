
-- 1. Nombre total d’appartements vendus au 1er semestre 2020.
--------------------
select count(*) as "nombre d'appart en 2020"
from bien
inner join vente
on bien.id=vente.id
where type_local="Appartement" and date_vente< "2020-07-01 00:00:00"
;
--------------------
-- 2. Le nombre de ventes d’appartement par région pour le 1er semestre
-- 2020.


select substr(localisation.code_postal,1 ,2) as "region", --on extrait les 2 premiers caractéres du code postal
count(vente.id) as "nombre de vente"
from bien
inner join vente
on bien.id=vente.id

inner join localisation
on bien.id=localisation.id
where type_local="Appartement" and date_vente< "2020-07-01 00:00:00"
group by region
;
--------------------
-- 3. Proportion des ventes d’appartements par le nombre de pièces.
-- avec une table temporaire
CREATE TEMPORARY TABLE totalnbreappart2 AS
SELECT COUNT(*) AS nombre_appart_2020
FROM bien
INNER JOIN vente
ON bien.id = vente.id
WHERE type_local = 'Appartement' AND date_vente < '2020-07-01 00:00:00';

SELECT nombre_pieces_principales,
ROUND(COUNT(nombre_pieces_principales)*100/(SELECT nombre_appart_2020 FROM totalnbreappart2),3) AS Pourcentage_nombre_de_pieces
FROM bien
INNER JOIN vente
ON bien.id = vente.id
WHERE type_local = 'Appartement' AND date_vente < '2020-07-01 00:00:00'
GROUP BY nombre_pieces_principales;

-- avec un WITH
WITH totalnbreappart AS (
SELECT COUNT(*) AS nombre_appart_2020
FROM bien
INNER JOIN vente
ON bien.id = vente.id
WHERE type_local = 'Appartement' AND date_vente < '2020-07-01 00:00:00'
)

SELECT nombre_pieces_principales,
ROUND(COUNT(nombre_pieces_principales)*100/(SELECT nombre_appart_2020 FROM totalnbreappart),3) AS Pourcentage_nombre_de_pieces
FROM bien
INNER JOIN vente
ON bien.id = vente.id
WHERE type_local = 'Appartement' AND date_vente < '2020-07-01 00:00:00'
GROUP BY nombre_pieces_principales;


-- --------------------
-- 4. Liste des 10 départements où le prix du mètre carré est le plus élevé.
select substr(localisation.code_postal,1 ,2) as "départemnetcode", --on extrait les 2 premiers caractéres du code postal
count(vente.id) as "nombre de vente",
round(avg(valeur_vente/surface_carrez),2) as "prix au m²"
from bien
inner join vente
on bien.id=vente.id

inner join localisation
on bien.id=localisation.id
where type_local="Appartement" and date_vente< "2020-07-01 00:00:00"
group by "départemnetcode"
ORDER by "prix au m²" DESC
limit 10
;



-- --------------------
-- 5. Prix moyen du mètre carré d’une maison en Île-de-France.
select substr(localisation.code_postal,1 ,2) as "départemnetcode", --on extrait les 2 premiers caractéres du code postal
count(vente.id) as "nombre de vente",
round(avg(valeur_vente/surface_carrez),2) as "prix au m²"
from bien
inner join vente
on bien.id=vente.id

inner join localisation
on bien.id=localisation.id
where type_local="Maison"
and départemnetcode in ("75","77","78","91","92","93","94")
and surface_carrez >0
and surface_reelle >0
group by "départemnetcode"
ORDER by "prix au m²" DESC

;


-- --------------------
-- 6. Liste des 10 appartements les plus chers avec la région et le nombre
-- de mètres carrés.
select substr(localisation.code_postal,1 ,2) as "départemnetcode", --on extrait les 2 premiers caractéres du code postal
count(vente.id) as "nombre de vente",
round(avg(valeur_vente/surface_carrez),2) as "prix au m²",
round(avg(surface_carrez),0) as "surface_réelle",
round(avg(surface_reelle),0)
from bien
inner join vente
on bien.id=vente.id

inner join localisation
on bien.id=localisation.id
where date_vente< "2020-07-01 00:00:00"
and départemnetcode in ("75","77","78","91","92","93","94")
and surface_carrez >0
and surface_reelle >0

group by "départemnetcode"
ORDER by "prix au m²" DESC

;



-- --------------------
-- 7. Taux d’évolution du nombre de ventes entre le premier et le second
-- trimestre de 2020.
-- Requête pour le premier trimestre
WITH
Q1 AS (
    SELECT COUNT(vente.id) AS "nombre de vente"
    FROM bien
    INNER JOIN vente ON bien.id=vente.id
    INNER JOIN localisation ON bien.id=localisation.id
    WHERE date_vente BETWEEN "2020-01-01 00:00:00" AND "2020-03-31 23:59:59"
    AND surface_carrez >0
    AND surface_reelle >0
),
Q2 AS (
    SELECT COUNT(vente.id) AS "nombre de vente"
    FROM bien
    INNER JOIN vente ON bien.id=vente.id
    INNER JOIN localisation ON bien.id=localisation.id
    WHERE date_vente BETWEEN "2020-04-01 00:00:00" AND "2020-06-30 23:59:59"
    AND surface_carrez >0
    AND surface_reelle >0
)
--calcul du taux d'évolution en % arrondi à 2 aprés la virgule
SELECT round(((Q2."nombre de vente" - Q1."nombre de vente") * 100.0 / Q1."nombre de vente"),2) || ' %' as "taux d'évolution"
FROM Q1, Q2;


-- 2éme solution avec un lag()





-- --------------------
-- 8. Le classement des régions par rapport au prix au mètre carré des
-- appartement de plus de 4 pièces.


-- --------------------
-- 9. Liste des communes ayant eu au moins 50 ventes au 1er trimestre


-- --------------------
-- 10. Différence en pourcentage du prix au mètre carré entre un
-- appartement de 2 pièces et un appartement de 3 pièces.


-- --------------------
-- 11. Les moyennes de valeurs foncières pour le top 3 des communes des
-- départements 6, 13, 33, 59 et 69.


-- --------------------
-- 12. Les 20 communes avec le plus de transactions pour 1000 habitants