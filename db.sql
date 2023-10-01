CREATE DATABASE IF NOT EXISTS TPS;
use TPS;

CREATE TABLE usuarios (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
        email VARCHAR(300) NOT NULL ,
        password  VARCHAR(100) NOT NULL,
        saldo FLOAT(10, 2) NOT NULL,
        fecha date not null
    )



    