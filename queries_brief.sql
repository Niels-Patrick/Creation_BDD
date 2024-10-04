/*
Les clients ayant consenti à recevoir des communications marketing
*/
SELECT * FROM Client
WHERE consentement_marketing = 1;

/*
Les commandes d'un client spécifique
*/
SELECT * FROM Commande
WHERE client_id = 63;

/*
Le montant total des commandes du client avec ID n° 61
*/
SELECT SUM(montant_commande) AS "Montant total" FROM Commande
WHERE client_id = 61;

/*
Les clients ayant passé des commandes de plus de 100 euros
*/
SELECT * FROM Client cl
JOIN Commande co
ON cl.client_id = co.client_id
WHERE montant_commande > 100;

/*
Les clients ayant passé des commandes après le 01/01/2023
*/
SELECT * FROM Client cl
JOIN Commande co
ON cl.client_id = co.client_id
WHERE date_commande > '2023:01:01';