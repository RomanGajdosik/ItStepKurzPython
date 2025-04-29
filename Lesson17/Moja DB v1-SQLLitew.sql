CREATE TABLE IF NOT EXISTS `Knihy` (
	`id` integer primary key NOT NULL UNIQUE,
	`Nazov` TEXT NOT NULL,
	`Autor` TEXT NOT NULL,
	`Rok_vydania` INTEGER NOT NULL,
	`Zaner` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Clenovia` (
	`id` integer primary key NOT NULL UNIQUE,
	`Meno` TEXT NOT NULL,
	`Priezvisko` TEXT NOT NULL,
	`email` TEXT NOT NULL,
	`datum_registracie` INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS `Autori` (
	`autor_id` integer primary key NOT NULL UNIQUE,
	`Meno` TEXT NOT NULL,
	`Datum_narodenia` INTEGER NOT NULL,
	`Krajina_povodu` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Vypozicky` (
	`vypozicky_id` integer primary key NOT NULL UNIQUE,
	`id_knihy` INTEGER NOT NULL,
	`id_clena` INTEGER NOT NULL,
	`datum_vypozicky` INTEGER NOT NULL,
	`datum_vratenia` INTEGER NOT NULL,
	`vratena_na_cas` REAL NOT NULL,
FOREIGN KEY(`id_knihy`) REFERENCES `Knihy`(`id`),
FOREIGN KEY(`id_clena`) REFERENCES `Clenovia`(`id`)
);
CREATE TABLE IF NOT EXISTS `knihy_autori` (
	`autor_id` INTEGER NOT NULL,
	`kniha_id` INTEGER NOT NULL,
FOREIGN KEY(`autor_id`) REFERENCES `Autori`(`autor_id`),
FOREIGN KEY(`kniha_id`) REFERENCES `Knihy`(`id`)
);