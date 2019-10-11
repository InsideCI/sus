CREATE DATABASE sigaa_ufpb;

\c sigaa_ufpb;

CREATE TABLE centros (
        id INT NOT NULL PRIMARY KEY,
        nome VARCHAR (100) NOT NULL
);

CREATE TABLE departamentos (
        id INT NOT NULL PRIMARY KEY,
        nome VARCHAR (100) NOT NULL,
        id_centro INT NOT NULL,
        FOREIGN KEY (id_centro) REFERENCES centros(id)
);

CREATE TABLE cursos (
        id INT NOT NULL PRIMARY KEY,
        nome VARCHAR (100) NOT NULL,
        cidade VARCHAR (100),
        tipo VARCHAR (100),
        coordenador VARCHAR (100) NOT NULL,
        id_centro INT NOT NULL,
        FOREIGN KEY (id_centro) REFERENCES centros(id)
);

CREATE TABLE turmas (
        id INT NOT NULL PRIMARY KEY,
        disciplina VARCHAR (100) NOT NULL,
        turma INT NOT NULL,
        professor VARCHAR (50) NOT NULL,
        horario VARCHAR (10) NOT NULL,
        sala VARCHAR(10),
        id_curso INT NOT NULL,
        FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

CREATE TABLE alunos (
        matricula VARCHAR(20) NOT NULL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        id_curso INT NOT NULL,
        FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

CREATE TABLE professores (
        id VARCHAR(20) NOT NULL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        grau VARCHAR(20) NOT NULL,
        id_departamento INT NOT NULL,
        FOREIGN KEY (id_departamento) REFERENCES departamentos(id)
);


