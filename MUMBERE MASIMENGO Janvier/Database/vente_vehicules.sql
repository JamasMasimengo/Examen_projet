-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 11 oct. 2024 à 06:15
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `vente_vehicules`
--

-- --------------------------------------------------------

--
-- Structure de la table `commande`
--

CREATE TABLE `commande` (
  `id` int(11) NOT NULL,
  `quantite` int(11) NOT NULL,
  `mode_paiement` varchar(100) NOT NULL,
  `dates` date NOT NULL,
  `id_panier` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `commande`
--

INSERT INTO `commande` (`id`, `quantite`, `mode_paiement`, `dates`, `id_panier`) VALUES
(1, 344, 'Paypal', '2024-10-26', 16),
(2, 2, 'Paypal', '2024-10-01', 20),
(3, 2, 'Paypal', '2024-10-09', 16),
(4, 1, 'Paypal', '2024-10-09', 21),
(5, 2, 'Paypal', '2024-10-07', 26),
(6, 34, 'Paypal', '2024-10-09', 27);

-- --------------------------------------------------------

--
-- Structure de la table `panier`
--

CREATE TABLE `panier` (
  `id` int(11) NOT NULL,
  `id_utilisateur` int(11) NOT NULL,
  `id_vehicule` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `panier`
--

INSERT INTO `panier` (`id`, `id_utilisateur`, `id_vehicule`) VALUES
(1, 6, 1),
(2, 6, 2),
(3, 6, 2),
(4, 6, 2),
(5, 0, 1),
(6, 0, 2),
(7, 0, 2),
(8, 0, 1),
(9, 0, 2),
(10, 0, 1),
(11, 0, 1),
(12, 0, 1),
(13, 0, 2),
(16, 14, 1),
(21, 14, 1),
(22, 14, 1),
(26, 15, 1),
(27, 14, 3),
(28, 14, 3);

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

CREATE TABLE `utilisateur` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`id`, `username`, `password`, `name`, `email`, `role`) VALUES
(12, 'jamas', '12345', 'janvier masimengo', 'masimengo@gmail.com', 'admin'),
(14, 'jamas2', '$2b$12$n5QfvFUuXW9AN69yS/RVOeB78EDmasqy7jqYn/q5JHDE08NsPdVkO', 'rtyuio', 'jamas2@gmail.com', 'client'),
(15, 'janvier', '$2b$12$c4cEdDSND2IS77ZsMfwbNuuLMzfiiKOz6objxF8fSXwYJ9NjrL2ei', 'masimengo', 'mb@gmail.com', 'client'),
(16, 'jamas3', '$2b$12$e22EzgsAM2ap5gcxIcz4nO8bfnUw2N1a9DsYfgZmBMd.wF9iJgMDa', 'masimengo', 'mb@gmail.com', 'client');

-- --------------------------------------------------------

--
-- Structure de la table `vehicule`
--

CREATE TABLE `vehicule` (
  `id` int(11) NOT NULL,
  `couleur` varchar(100) NOT NULL,
  `modele` varchar(100) NOT NULL,
  `marque` varchar(100) NOT NULL,
  `prix` float NOT NULL,
  `categorie` varchar(100) NOT NULL,
  `photo` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `age` int(11) NOT NULL,
  `kilometrage` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `vehicule`
--

INSERT INTO `vehicule` (`id`, `couleur`, `modele`, `marque`, `prix`, `categorie`, `photo`, `description`, `age`, `kilometrage`) VALUES
(1, 'rouge', 'Fiat-500', 'Toyota', 34444, 'Mini-citadines', 'ferrari.jpg', 'vehicule adapte dans des regions montagneuses', 2, 3),
(3, 'rose', 'Fiat-500', 'Toyota', 3456, 'Voitures de sport', 'ferrari.jpg', 'ertyuioujff', 0, 0);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `commande`
--
ALTER TABLE `commande`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_panier` (`id_panier`);

--
-- Index pour la table `panier`
--
ALTER TABLE `panier`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_utilisateur` (`id_utilisateur`),
  ADD KEY `id_vehicule` (`id_vehicule`);

--
-- Index pour la table `utilisateur`
--
ALTER TABLE `utilisateur`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `vehicule`
--
ALTER TABLE `vehicule`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `commande`
--
ALTER TABLE `commande`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `panier`
--
ALTER TABLE `panier`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT pour la table `utilisateur`
--
ALTER TABLE `utilisateur`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT pour la table `vehicule`
--
ALTER TABLE `vehicule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
