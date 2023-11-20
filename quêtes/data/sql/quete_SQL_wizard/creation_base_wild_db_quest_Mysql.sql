DROP DATABASE IF EXISTS "wild_db_quest";
CREATE DATABASE IF NOT EXISTS "wild_db_quest";

USE "wild_db_quest";
DROP TABLE IF EXISTS "wizard";

CREATE TABLE "wizard" (
    "id" INT NOT NULL AUTO_INCREMENT,
    "firstname" VARCHAR(100) NOT NULL,
    "lastname" VARCHAR(100) NOT NULL,
    "birthday" DATE NOT NULL,
    "birth_place" VARCHAR(255) NULL,
    "biography" TEXT NULL,
    "is_muggle" BOOLEAN NOT NULL,
    PRIMARY KEY ("id")
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

