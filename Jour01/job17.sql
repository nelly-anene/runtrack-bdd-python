--Modifier l'age de Betty Spaghetti de 23 a 20 ans
UPDATE etudiants SET age = 20 WHERE prenom = 'Betty' AND nom = 'Spaghetti';

SELECT * FROM etudiants WHERE prenom = 'Betty';