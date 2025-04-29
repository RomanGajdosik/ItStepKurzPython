CREATE TABLE [Knihy] (
	[id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[Nazov] nvarchar(max) NOT NULL,
	[Autor] nvarchar(max) NOT NULL,
	[Rok_vydania] int NOT NULL,
	[Zaner] nvarchar(max) NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [Clenovia] (
	[id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[Meno] nvarchar(max) NOT NULL,
	[Priezvisko] nvarchar(max) NOT NULL,
	[email] nvarchar(max) NOT NULL,
	[datum_registracie] int NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [Autori] (
	[autor_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[Meno] nvarchar(max) NOT NULL,
	[Datum_narodenia] int NOT NULL,
	[Krajina_povodu] nvarchar(max) NOT NULL,
	PRIMARY KEY ([autor_id])
);

CREATE TABLE [Vypozicky] (
	[vypozicky_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[id_knihy] int NOT NULL,
	[id_clena] int NOT NULL,
	[datum_vypozicky] int NOT NULL,
	[datum_vratenia] int NOT NULL,
	[vratena_na_cas] bit NOT NULL,
	PRIMARY KEY ([vypozicky_id])
);

CREATE TABLE [knihy_autori] (
	[autor_id] int NOT NULL,
	[kniha_id] int NOT NULL
);




ALTER TABLE [Vypozicky] ADD CONSTRAINT [Vypozicky_fk1] FOREIGN KEY ([id_knihy]) REFERENCES [Knihy]([id]);

ALTER TABLE [Vypozicky] ADD CONSTRAINT [Vypozicky_fk2] FOREIGN KEY ([id_clena]) REFERENCES [Clenovia]([id]);
ALTER TABLE [knihy_autori] ADD CONSTRAINT [knihy_autori_fk0] FOREIGN KEY ([autor_id]) REFERENCES [Autori]([autor_id]);

ALTER TABLE [knihy_autori] ADD CONSTRAINT [knihy_autori_fk1] FOREIGN KEY ([kniha_id]) REFERENCES [Knihy]([id]);