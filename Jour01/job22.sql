--Etudiant le plus jeune
SELECT * FROM etudiants WHERE age = (SELECT MIN(age) FROM etudiants);