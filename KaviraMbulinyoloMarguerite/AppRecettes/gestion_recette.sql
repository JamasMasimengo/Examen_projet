-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 08 oct. 2024 à 15:07
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
-- Base de données : `gestion_recette`
--

-- --------------------------------------------------------

--
-- Structure de la table `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `transaction`
--

CREATE TABLE `transaction` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `amount` decimal(10,2) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `transaction`
--

INSERT INTO `transaction` (`id`, `user_id`, `amount`, `type`, `description`, `date`) VALUES
(1, 1, 20.00, 'income', '0', NULL),
(2, 1, 35.00, 'expense', '0', NULL),
(3, 2, 100.00, 'expense', '0', NULL),
(4, 1, 50.00, 'expense', '0', NULL),
(6, 1, 6000.00, 'income', '0', NULL),
(7, 1, 200.00, 'expense', '0', NULL),
(9, 1, 19.00, 'expense', '0', NULL),
(10, 1, 50.00, '', NULL, '2024-10-07'),
(11, 1, 89.00, '', NULL, '2024-10-07'),
(12, 1, 87.00, 'revenu', NULL, '2024-10-07'),
(13, 1, 98.00, 'dépense', 'achat phone', '2024-10-07'),
(14, 3, 78.00, 'revenu', 'Ventes fournitures', '2024-10-07'),
(15, 1, 43.00, 'dépense', 'Electricité', '2024-10-07'),
(16, 7, 23.00, 'dépense', 'Nourriture', '2024-10-08'),
(17, 8, 56.00, 'dépense', 'Electricité', '2024-10-08'),
(18, 12, 78.00, 'dépense', 'Achat fournitures', '2024-10-08'),
(19, 8, 100.00, 'revenu', 'Vente ordinateurs', '2024-10-08'),
(20, 13, 76.00, 'dépense', 'Payement Electricité', '2024-10-08');

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(150) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id`, `username`, `password`) VALUES
(6, 'MKM', '$2b$12$0hJItw3dn9YvWHuZp0j23e8Hk5IlRQ931Nz1uapvgtKAFPHlyOflG'),
(7, 'Marguerite', '$2b$12$VMpn1.tlVzEjs1UiQZRJCeODZLJnQ0lk5yTx8mW805DsrxLMrMrfm'),
(8, 'Maggy', '$2b$12$.3wk1fkWl3iCHKbC20cqzOD0Im5DeR0dvn17SYsHCleDom2Wpgla.'),
(9, 'Kavira', '$2b$12$w1cbrxkR8xUyt90.Uh2XWuGBb3Kv4TuZ5XKCS1F6nBzSjtHdbAJ6i'),
(10, 'Ange', '$2b$12$Kt71G.a2kAGvSQj3Pe.a9ejGGcJVgj9fyvrw44yDOt.AUgI1VBpSC'),
(11, 'Muyisa', '$2b$12$OW9R3JADmM5h66CnY.8xouh6mwnQbhAqAScW0VT11t2n9mqLCRD0e'),
(12, 'Mgy', '$2b$12$dhemsNj4VWvC8c0LUBlq5e3yHg12lFTp.se2lbhjnfW/rGVoSqLIa'),
(13, 'Mumbere', '$2b$12$aJvBhd9Utny54NyqKRsktOoNzVk6A8xZ4OOcjv7cTS5mQfbn1j7CS');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
