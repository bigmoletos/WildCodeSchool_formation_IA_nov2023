-- 1 Ventes: Le nombre de produits vendus par catégorie et par mois, avec comparaison et taux d’évolution par rapport au même mois de l’année précédente.
WITH sales AS (
  SELECT 
    YEAR(o.orderDate) AS year,
    DATE_FORMAT(o.orderDate, '%M') AS month,
    p.productLine AS category,
    SUM(od.quantityOrdered) AS products_sold
  FROM 
    orders o
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
    JOIN products p ON od.productCode = p.productCode
  GROUP BY 
    year, month, category
),
sales_comparison AS (
  SELECT 
    s1.year,
    s1.month,
    s1.category,
    s1.products_sold,
    s2.products_sold AS products_sold_last_year,
    CONCAT(ROUND((s1.products_sold - s2.products_sold) / s2.products_sold * 100, 2), ' %') AS growth_rate
  FROM 
    sales s1
    LEFT JOIN sales s2 ON s1.year = s2.year + 1 AND s1.month = s2.month AND s1.category = s2.category
)
SELECT * FROM sales_comparison
order by growth_rate desc ;


-- 2-Finances: Le chiffre d’affaires des commandes des deux derniers mois par pays.
SELECT 
  MAX(o.orderDate) AS latest_order_date  -- pour connaitre la derniére commande
FROM 
  orders o;
 
SELECT 
  c.country,
  SUM(od.quantityOrdered * od.priceEach) AS "chiffre d'affaire"
FROM 
  customers c
  JOIN orders o ON c.customerNumber = o.customerNumber
  JOIN orderdetails od ON o.orderNumber = od.orderNumber
WHERE 
  o.orderDate >= (
    SELECT MAX(orderDate) FROM orders
  ) - INTERVAL 2 MONTH
GROUP BY 
  c.country
 order by "chiffre d'affaire" asc ;


 
--  3-Commandes qui n’ont pas encore été payées.
 
SELECT DISTINCT status FROM orders; -- pour connaitre les différents statuts

SELECT 
  o.orderNumber,
  o.orderDate,
  c.customerNumber,
  c.customerName,
  o.status
FROM 
  orders o
  JOIN customers c ON o.customerNumber = c.customerNumber
WHERE 
  o.status  != 'Resolved'
 ;

 
--  4-Logistique: Le stock des 5 produits les plus commandés.
 SELECT 
  p.productCode,
  p.productName,
  p.quantityInStock
FROM 
  products p
JOIN 
  (
    SELECT 
      od.productCode,
      SUM(od.quantityOrdered) AS total_quantity
    FROM 
      orderdetails od
    GROUP BY 
      od.productCode
    ORDER BY 
      total_quantity DESC
    LIMIT 5
  ) AS most_ordered
ON 
  p.productCode = most_ordered.productCode;

 
--  5-Ressources humaines: Chaque mois, les 2 vendeurs avec le CA le plus élevé.
 WITH monthly_sales AS (
  SELECT 
    EXTRACT(YEAR FROM o.orderDate) AS year,
   DATE_FORMAT(o.orderDate, '%M') AS month,
    e.firstName,
    e.lastName,
    SUM(od.quantityOrdered * od.priceEach) AS revenue
  FROM 
    employees e
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    JOIN orders o ON c.customerNumber = o.customerNumber
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
  GROUP BY 
    year, month, e.firstName, e.lastName
)
SELECT 
  m1.year,
  m1.month,
  m1.firstName,
  m1.lastName,
  m1.revenue
FROM 
  monthly_sales m1
WHERE 
  (
    SELECT 
      COUNT(*)
    FROM 
      monthly_sales m2
    WHERE 
      m1.year = m2.year AND m1.month = m2.month AND m1.revenue < m2.revenue
  ) < 2
ORDER BY 
  m1.year, m1.month;

 
 

