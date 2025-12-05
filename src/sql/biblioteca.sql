DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE livros(
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100)
);

SELECT id, titulo FROM livros;

ALTER TABLE livros ADD COLUMN quantidade_paginas INT;

SELECT id, titulo, quantidade_paginas FROM livros;

ALTER TABLE livros ADD COLUMN autor VARCHAR(100);
ALTER TABLE livros ADD COLUMN preco DOUBLE;
ALTER TABLE livros ADD COLUMN isbn VARCHAR(100);
ALTER TABLE livros ADD COLUMN descricao TEXT;

SELECT id, titulo, quantidade_paginas, autor, preco, isbn, descricao FROM livros;

CREATE TABLE mangas(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    volume INT,
    autor VARCHAR(100),
    data_lancamento DATE
);

INSERT INTO mangas (nome, volume, autor, data_lancamento) VALUES ("Naruto", 52, "Masashi Kishimoto", "2010-08-04"),
("Dragon Ball", 20, "Akima Toriyama", "1990-01-10");

INSERT INTO mangas (nome, volume, autor, data_lancamento) VALUE ("Teste", 1, "EU", "2025-12-05");