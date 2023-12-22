/*quete_SQL3_manipulation des données*/
SET SQL_SAFE_UPDATES = 0;
USE `wild_db_quest`;
DROP TABLE IF EXISTS `school`; 
CREATE TABLE `school` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
    `capacity` INT,
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;  

ALTER TABLE school
ADD country VARCHAR(255);


INSERT INTO school (name, country, capacity) 
VALUES 
('Beauxbatons Academy of Magic', 'France', 550), 
('Castelobruxo', 'Brazil', 380), 
('Durmstrang Institute', 'Norway', 570),
('Hogwarts School of Witchcraft and Wizardry', 'United Kingdom', 450),
('IlvermoRny School Witchcraft and Wizardy ','USA',300),
('Koldovstoretz','Russia',125),
('Mahoutokoro School of magic','Japan',800),
('Uagadou School of magic','Uganda',350);



UPDATE school 
SET 
    country = 'Sweden'
WHERE
    name LIKE 'Durmstrang%';

UPDATE school 
SET 
    capacity = 700
WHERE
    name LIKE 'Mahoutokoro%';

DELETE FROM school 
WHERE
    name LIKE '%magic%';

SELECT 
    *
FROM
    school;