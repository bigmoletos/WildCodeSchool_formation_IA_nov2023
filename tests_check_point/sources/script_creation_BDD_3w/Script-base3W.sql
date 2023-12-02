-- Ton code SQL ici :
use w3schools;
SELECT c.CategoryName, 
ROUND(SUM(p.Price*od.Quantity)) as Chiffre_d_affaire, 
ROUND(SUM(p.Price*od.Quantity)/SUM(od.Quantity),2) as Prix_moyen
FROM Categories c
JOIN Products p 
ON c.CategoryID=p.CategoryID
JOIN Order_Details od 
ON p.ProductID=od.ProductID
GROUP BY c.CategoryID
ORDER BY Chiffre_d_affaire DESC;
        