BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER NOT NULL,
	"username"	TEXT NOT NULL,
	"hash"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "mechanics" (
	"id_mechanics"	integer NOT NULL,
	"Name"	text NOT NULL,
	"Description"	text,
	PRIMARY KEY("id_mechanics" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "collection" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"Name"	text NOT NULL,
	"Description"	text,
	"Players"	integer NOT NULL,
	"Age"	integer NOT NULL,
	"Duration"	integer NOT NULL,
	"Category"	text,
	"Id_Mechanics"	integer NOT NULL,
	"datetime"	 NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE UNIQUE INDEX IF NOT EXISTS "username" ON "users" (
	"username"
);

INSERT INTO	mechanics (name, Description) VALUES ("area control", "Controla uma área comum aos jogadores")
INSERT INTO	mechanics (name, Description) VALUES ("Draft", "Os jogadores trocam de cartas")

COMMIT;
