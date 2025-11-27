SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `unify` DEFAULT CHARACTER SET utf8 ;
USE `unify` ;

CREATE TABLE IF NOT EXISTS `unify`.`Artista` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome_artista` VARCHAR(100) NOT NULL,
  `pais` VARCHAR(80) NOT NULL,
  `streamings_mensal` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `unify`.`Genero` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome_genero` VARCHAR(45) NOT NULL,
  `descricao` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `unify`.`Album` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome_album` VARCHAR(100) NOT NULL,
  `ano_lancamento` YEAR NOT NULL,
  `id_artista` INT NOT NULL,
  `id_genero` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `album_artista_idx` (`id_artista` ASC) VISIBLE,
  INDEX `album_genero_idx` (`id_genero` ASC) VISIBLE,
  CONSTRAINT `album_artista`
    FOREIGN KEY (`id_artista`)
    REFERENCES `unify`.`Artista` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `album_genero`
    FOREIGN KEY (`id_genero`)
    REFERENCES `unify`.`Genero` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `unify`.`Musica` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome_musica` VARCHAR(100) NOT NULL,
  `streamings_numero` INT NOT NULL,
  `duracao` TIME NOT NULL,
  `id_album` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `musica_album_idx` (`id_album` ASC) VISIBLE,
  CONSTRAINT `musica_album`
    FOREIGN KEY (`id_album`)
    REFERENCES `unify`.`Album` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

ALTER TABLE `unify`.`Musica` 
MODIFY COLUMN `streamings_numero` BIGINT;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
