DROP TABLE IF EXISTS wizard;

CREATE TABLE wizard (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    birthday DATE NOT NULL,
    birth_place VARCHAR(255),
    biography TEXT,
    is_muggle BOOLEAN NOT NULL
);


