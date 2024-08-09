CREATE DATABASE IF NOT EXISTS nombre_base_datos;
USE nombre_base_datos;

CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_empresa VARCHAR(100),
    usuario VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    tipo_usuario VARCHAR(20) NOT NULL
);

CREATE TABLE Group (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    usuario_empresa_id INT NOT NULL,
    FOREIGN KEY (usuario_empresa_id) REFERENCES User(id)
);

CREATE TABLE Survey (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    usuario_superadmin_id INT NOT NULL,
    FOREIGN KEY (usuario_superadmin_id) REFERENCES User(id)
);

CREATE TABLE Question (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(500) NOT NULL,
    encuesta_id INT NOT NULL,
    FOREIGN KEY (encuesta_id) REFERENCES Survey(id)
);

CREATE TABLE Answer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(500) NOT NULL,
    pregunta_id INT NOT NULL,
    FOREIGN KEY (pregunta_id) REFERENCES Question(id)
);

CREATE TABLE ActivityLog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    actividad VARCHAR(500) NOT NULL,
    fecha_hora DATETIME NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES User(id)
);
