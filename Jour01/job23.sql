--Etudiant le plus age
SELECT * FROM etudiants WHERE age = (SELECT MAX(age) FROM etudiants);