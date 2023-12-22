-- Affiche les valeurs des employés dont le nom de famille a comme 2ème la lettre "a", "b", "c", ou "z"
SELECT * FROM Employees WHERE SUBSTRING(firstname,2,1)  IN ('a', 'b', 'c', 'z');

-- Affiche les noms des clients qui n'ont jamais acheté de produit en 
-- rangeant leurs noms en ordre alphabétique inversé
SELECT c.CustomerName 
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID=o.CustomerID
WHERE o.CustomerID IS NULL
ORDER BY c.CustomerName DESC;


-- Quel est le prix moyen de tous les produits ?
SELECT AVG(o.Quantity * p.Price) as "moyenne"
FROM Products p
INNER JOIN OrderDetails o ON o.ProductId=p.ProductId;


-- Affiche toutes les lignes des produits de la catégorie la plus souvent vendue
WITH categorie_la_plus_vendu AS (
    SELECT p.CategoryID
    FROM Products p
    JOIN OrderDetails o ON p.ProductID = o.ProductID
    GROUP BY p.CategoryID
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
SELECT p.*
FROM Products p
JOIN categorie_la_plus_vendu cv ON p.CategoryID = cv.CategoryID;



-- Afficher les pays d'origine des fournisseurs qui produisent des produits de plus de plus de 3 euros
SELECT DISTINCT ct.CategoryName
FROM Products p
LEFT JOIN Categories ct ON ct.CategoryID = p.CategoryID
WHERE p.CategoryID = 3
LIMIT 1;

/* Créez une requête SQL qui renvoie les noms de chaque catégorie, 
le chiffre d'affaires associé à chaque catégorie et le prix moyen pondéré des produits vendus dans cette catégorie.

Le chiffre d'affaires doit être arrondi à l'unité supérieure et le prix moyen doit comporter 2 décimales.

Ce tableau doit être trié pour afficher en premier les catégories avec le chiffre d'affaires le plus élevé.

Le code SQL devra être copié/collé dans un bloc de code ci-dessous.*/

SELECT categoryname, 
ROUND(SUM(o.quantity * p.price), 0) AS "Chiffre d'affaire",
ROUND(sum(o.quantity * p.price)/ SUM(o.quantity), 2) AS "prix moyen pondéré"
FROM products p, categories c, orderdetails o
WHERE p.categoryid = c.categoryid
AND p.productid = o.productid
GROUP BY categoryname
ORDER BY categoryname;










