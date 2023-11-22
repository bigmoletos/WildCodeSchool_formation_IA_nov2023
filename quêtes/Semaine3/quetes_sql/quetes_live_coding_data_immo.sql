
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



-- --------------------
-- 5. Prix moyen du mètre carré d’une maison en Île-de-France.



-- --------------------
-- 6. Liste des 10 appartements les plus chers avec la région et le nombre
-- de mètres carrés.



-- --------------------
-- 7. Taux d’évolution du nombre de ventes entre le premier et le second
-- trimestre de 2020.


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