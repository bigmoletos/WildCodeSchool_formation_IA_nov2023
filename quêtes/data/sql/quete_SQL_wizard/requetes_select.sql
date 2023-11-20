-- selection age
SELECT *
FROM wizard
WHERE birthday BETWEEN '1975-01-01' AND '1985-01-01';
--selection noms commencant par H
SELECT firstname
FROM wizard
WHERE firstname LIKE 'H%';
-- selection du prenom
SELECT firstname, lastname
FROM wizard
WHERE lastname = 'potter'
ORDER BY firstname;

--selection aniversaires

SELECT firstname, lastname, birthday
FROM wizard
ORDER BY birthday
LIMIT 1;

