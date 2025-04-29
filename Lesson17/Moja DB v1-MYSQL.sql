CREATE TABLE IF NOT EXISTS `Knihy` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`Nazov` varchar(255) NOT NULL,
	`Autor` varchar(255) NOT NULL,
	`Rok_vydania` int NOT NULL,
	`Zaner` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Clenovia` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`Meno` varchar(255) NOT NULL,
	`Priezvisko` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL,
	`datum_registracie` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Autori` (
	`autor_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`Meno` varchar(255) NOT NULL,
	`Datum_narodenia` int NOT NULL,
	`Krajina_povodu` varchar(255) NOT NULL,
	PRIMARY KEY (`autor_id`)
);

CREATE TABLE IF NOT EXISTS `Vypozicky` (
	`vypozicky_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`id_knihy` int NOT NULL,
	`id_clena` int NOT NULL,
	`datum_vypozicky` int NOT NULL,
	`datum_vratenia` int NOT NULL,
	`vratena_na_cas` boolean NOT NULL,
	PRIMARY KEY (`vypozicky_id`)
);

CREATE TABLE IF NOT EXISTS `knihy_autori` (
	`autor_id` int NOT NULL,
	`kniha_id` int NOT NULL
);




ALTER TABLE `Vypozicky` ADD CONSTRAINT `Vypozicky_fk1` FOREIGN KEY (`id_knihy`) REFERENCES `Knihy`(`id`);

ALTER TABLE `Vypozicky` ADD CONSTRAINT `Vypozicky_fk2` FOREIGN KEY (`id_clena`) REFERENCES `Clenovia`(`id`);
ALTER TABLE `knihy_autori` ADD CONSTRAINT `knihy_autori_fk0` FOREIGN KEY (`autor_id`) REFERENCES `Autori`(`autor_id`);

ALTER TABLE `knihy_autori` ADD CONSTRAINT `knihy_autori_fk1` FOREIGN KEY (`kniha_id`) REFERENCES `Knihy`(`id`);