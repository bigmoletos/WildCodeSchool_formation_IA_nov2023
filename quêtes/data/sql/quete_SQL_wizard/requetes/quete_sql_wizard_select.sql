DROP DATABASE IF EXISTS `wild_db_quest`;
CREATE DATABASE IF NOT EXISTS `wild_db_quest`;

USE `wild_db_quest`;
DROP TABLE IF EXISTS `wizard`;

CREATE TABLE `wizard` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `firstname` VARCHAR(100) NOT NULL,
    `lastname` VARCHAR(100) NOT NULL,
    `birthday` DATE NOT NULL,
    `birth_place` VARCHAR(255) NULL,
    `biography` TEXT NULL,
    `is_muggle` BOOLEAN NOT NULL,
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

 DROP TABLE IF EXISTS `school`;
CREATE TABLE `school` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
     `country` VARCHAR(100) NOT NULL,
    `capacity` INT,
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('harry', 'potter', '1980-07-31', 'london', '', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('hermione', 'granger', '1979-09-19', '', 'Friend of Harry Potter', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('lily', 'potter', '1960-01-30', '', 'mother of Harry Potter', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('ron', 'weasley', '1980-03-01', '', 'Best friend of Harry', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('ginny', 'weasley', '1981-08-11', '', 'Sister of Ron and girlfriend of Harry', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('fred', 'weasley', '1978-04-01', '', '', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('george', 'weasley', '1978-04-01', '', '', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('arthur', 'weasley', '1950-02-06', '', '', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('molly', 'weasley', ' 1949-01-01', '', '', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('drago', 'malefoy', '1980-06-05', '', '', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('albus', 'dumbledore', '1881-07-01', '', '', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('severus', 'rogue', '1960-01-09', '', '', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('tom', 'jÃ©dusor', '1926-12-31', '', 'Celui-Dont-On-Ne-Doit-Pas-Prononcer-Le-Nom alias Voldermort', '0');
INSERT INTO `wild_db_quest`.`wizard` (`firstname`, `lastname`, `birthday`, `birth_place`, `biography`, `is_muggle`) VALUES ('dudley', 'dursley', '1980-06-23', '', 'Cousin d''Harry', '1');


INSERT INTO school (name, country, capacity)
VALUES
('Beauxbatons Academy of Magic', 'France', 550),
('Castelobruxo', 'Brazil', 380),
('Durmstrang Institute', 'Norway', 570),
('Hogwarts School of Witchcraft and Wizardry', 'United Kingdom', 450),
('IlvermoRny School Witchcraft and Wizardy ','USA',300),
('Koldovstoretz','Russia',125),
('Mahoutokoro School of magic','Japan',800),
('Uagadou School of magic','Uganda',350),
('Bossancourt tradition', 'France',312 ),
('Tocapuria', 'Brazil', 67),
('Kiopler ', 'Norway', 765),
('OldStudent School of Witchcraft and Wizardry', 'United Kingdom',90),
('Wit School Witchcraft and Wizardy ','USA',543),
('Loudmila','Russia',98),
('Yamathi School of magic','Japan',76),
('Tambouktou School of magic','Uganda',765);
