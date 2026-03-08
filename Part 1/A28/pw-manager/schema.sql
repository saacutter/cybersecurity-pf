DROP TABLE IF EXISTS passwords;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id                 INTEGER PRIMARY KEY NOT NULL,
    username           TEXT UNIQUE NOT NULL,
    master_password    TEXT NOT NULL,
    salt               BLOB NOT NULL
);

CREATE TABLE passwords (
    id              INTEGER PRIMARY KEY NOT NULL,
    user_id         INT NOT NULL,
    name            TEXT NOT NULL,
    username        TEXT,
    password        TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);