CREATE DATABASE sigaa_ufpb;

\c sigaa_ufpb;

CREATE TABLE centro (
        id INT NOT NULL PRIMARY KEY,
        nome VARCHAR (100) NOT NULL
);

CREATE TABLE departamento (
        id INT NOT NULL PRIMARY KEY,
        nome VARCHAR (100) NOT NULL,
        id_centro INT NOT NULL,
        FOREIGN KEY (id_centro) REFERENCES centro (id)
);

CREATE TABLE curso (
        id INT NOT NULL PRIMARY KEY,
        nome VARCHAR (100) NOT NULL,
        coordenador VARCHAR (100) NOT NULL,
        id_departamento INT NOT NULL,
        FOREIGN KEY (id_departamento) REFERENCES departamento(id)
);

CREATE TABLE turma (
        id INT NOT NULL PRIMARY KEY,
        disciplina VARCHAR (100) NOT NULL,
        turma INT NOT NULL,
        professor VARCHAR (50) NOT NULL,
        horario VARCHAR (10) NOT NULL,
        sala VARCHAR(10),
        id_curso INT NOT NULL,
        FOREIGN KEY (id_curso) REFERENCES curso(id)
);

CREATE TABLE aluno (
        matricula VARCHAR(20) NOT NULL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        id_curso INT NOT NULL,
        FOREIGN KEY (id_curso) REFERENCES curso(id)
);

CREATE TABLE professor (
        id VARCHAR(20) NOT NULL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        grau VARCHAR(20) NOT NULL,
        id_departamento INT NOT NULL,
        FOREIGN KEY (id_departamento) REFERENCES departamento(id)
);


