DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE livros(
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100)
);

SELECT id, titulo FROM livros;

ALTER TABLE livros ADD COLUMN quantidade_paginas DOUBLE;

ALTER TABLE livros MODIFY COLUMN quantidade_paginas INT;

SELECT id, titulo, quantidade_paginas FROM livros;

ALTER TABLE livros ADD COLUMN autor VARCHAR(100);
ALTER TABLE livros ADD COLUMN preco DOUBLE;
ALTER TABLE livros ADD COLUMN isbn VARCHAR(100);
ALTER TABLE livros ADD COLUMN descricao TEXT;

SELECT id, titulo, quantidade_paginas, autor, isbn,