-- Insertion des données dans l'etage
-- Ajoute 2 étages : le RDC et le R+1
INSERT INTO etage (nom, numero, superficie) VALUES
('RDC', 0, 500),
('R+1', 1, 500);

-- Insertion des données la table salle
-- Ajoute 6 salles, chacune liée à un étage via id_etage
INSERT INTO salle (nom, id_etage, capacite) VALUES
('Lounge', 1, 100),
('Studio Son', 1, 5),
('Broadcasting', 2, 50),
('Bocal Peda', 2, 4),
('Coworking', 2, 80),
('Studio Video', 2, 5);