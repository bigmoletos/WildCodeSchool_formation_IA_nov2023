-- crée une requête SQL qui fournit les noms de chaque catégorie, le chiffre d'affaire
-- associé à cette catégorie, et le prix moyen pondéré des produits vendus pour cette catégorie. 
-- Le chiffre d'affaire sera arrondi à l'unité la plus proche, et le prix moyen comportera 2 décimales.
-- Ce tableau devra être trié pour avoir les catégories avec le chiffre d'affaire le plus élevé en premier.

USE w3schools;
with PrixMoyen as(
select 
ROUND((SUM(p.Price*od.Quantity)/SUM(od.Quantity)),2) as "Prix moyen"
from categories c 
join products p using(id) 

);
-- autre solution
SELECT c.CategoryName as "Catégories", 
ROUND(SUM(p.Price*od.Quantity)) as "Chiffre d'affaire", 
ROUND((SUM(p.Price*od.Quantity)/SUM(od.Quantity)),2) as "Prix moyen"
FROM Categories c
JOIN Products p using(id) 
JOIN Order_Details od using(id) 
GROUP BY c.CategoryID
ORDER BY "Chiffre d'affaire" DESC;

/* select CONCAT(firstname, ' ', lastname) AS fullname, role
from player p 
inner join wizard w  using(id) 
where enrollment_date between '1995-01-01' and '1998-01-01'
and role='chaser'
;
*/
-- autre solution
SELECT c.CategoryName as "Catégories", 
ROUND(SUM(p.Price*od.Quantity)) as "Chiffre d'affaire", 
ROUND((SUM(p.Price*od.Quantity)/SUM(od.Quantity)),2) as "Prix moyen"
FROM Categories c
JOIN Products p 
ON c.CategoryID=p.CategoryID
JOIN Order_Details od 
ON p.ProductID=od.ProductID
GROUP BY c.CategoryID
ORDER BY "Chiffre d'affaire" DESC;
        