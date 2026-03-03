-- Ajouter Martin Dupuis et recherche des membres d'une meme famille
INSERT INTO etudiants (nom, prenom, age, email) VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');

SELECT * FROM etudiants WHERE nom = 'Dupuis';