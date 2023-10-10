CREATE DATABASE IF NOT EXISTS MUSIC;
use MUSIC;

CREATE TABLE usuarios (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        usuario VARCHAR(50) NOT NULL,
        password  VARCHAR(100) NOT NULL,
        fecha date not null
    )

CREATE TABLE listas_de_reproduccion (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    usuario_id INT(11) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
