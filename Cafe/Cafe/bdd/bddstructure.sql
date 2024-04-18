CREATE DATABASE IF NOT EXISTS `cafeteria`;
USE `cafeteria`;

CREATE TABLE IF NOT EXISTS `cliente` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(30) NOT NULL,
    `apellido` VARCHAR(30) NOT NULL,
    `email` VARCHAR(50),
    `telefono` CHAR(10),
    `direccion` VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS `producto` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(50) NOT NULL,
    `descripcion` VARCHAR(255) NOT NULL,
    `precio` FLOAT NOT NULL,
    `stock` INT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS `pedido` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `id_producto` INT NOT NULL,
    `id_cliente` INT NOT NULL,
    `fecha` DATETIME NOT NULL,
    `total` FLOAT NOT NULL,
    `estado` CHAR(1) NOT NULL DEFAULT '0', -- 0 = pendiente, 1 = entregado
    `cantidad` INT NOT NULL DEFAULT 0,
    FOREIGN KEY (`id_producto`) REFERENCES `producto`(`id`),
    FOREIGN KEY (`id_cliente`) REFERENCES `cliente`(`id`)
);

ALTER TABLE `cliente`
ADD CONSTRAINT unq_email UNIQUE (`email`);

ALTER TABLE `producto`
ADD CONSTRAINT unq_nombre UNIQUE (`nombre`);
