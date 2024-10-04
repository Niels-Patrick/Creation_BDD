CREATE TABLE IF NOT EXISTS "Client" (
	"client_id" INTEGER NOT NULL UNIQUE,
	"nom" VARCHAR NOT NULL,
	"prenom" VARCHAR NOT NULL,
	"email" VARCHAR NOT NULL UNIQUE,
	"telephone" VARCHAR,
	"date_naissance" DATE,
	"adresse" VARCHAR,
	"consentement_marketing" BOOLEAN NOT NULL,
	PRIMARY KEY("client_id")
);

CREATE TABLE IF NOT EXISTS "Commande" (
	"commande_id" INTEGER NOT NULL UNIQUE,
	"client_id" INTEGER NOT NULL,
	"date_commande" DATE NOT NULL,
	"montant_commande" REAL NOT NULL,
	PRIMARY KEY("commande_id"),
	FOREIGN KEY ("client_id") REFERENCES "Client"("client_id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);
