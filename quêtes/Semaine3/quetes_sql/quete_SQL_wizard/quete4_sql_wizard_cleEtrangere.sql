/*quete_SQL3_manipulation des données*/
SET SQL_SAFE_UPDATES = 0;
USE `wild_db_quest`;
DROP TABLE IF EXISTS `wizard`; 
DROP TABLE IF EXISTS `wizard`;

CREATE TABLE `wizard` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `firstname` VARCHAR(100) NOT NULL,
    `lastname` VARCHAR(100) NOT NULL,
    `birthday` DATE NOT NULL,
    `birth_place` VARCHAR(255) NULL,
    `biography` TEXT NULL,
    `is_muggle` BOOLEAN NOT NULL,
    PRIMARY KEY (`id`),
    school_id INT NOT NULL,
    CONSTRAINT fk_wizard_school FOREIGN KEY (school_id)
        REFERENCES school (id)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8;
       


/*
ALTER TABLE wizard
ADD CONSTRAINT fk_wizard_school 
FOREIGN KEY (school_id) 
REFERENCES school(id);
*/

