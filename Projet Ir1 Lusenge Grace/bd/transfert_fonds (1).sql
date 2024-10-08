-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 07 oct. 2024 à 22:01
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
-- Base de données : `transfert_fonds`
--

-- --------------------------------------------------------

--
-- Structure de la table `clients`
--

CREATE TABLE `clients` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `adresse` varchar(50) NOT NULL,
  `Telephone` varchar(15) NOT NULL,
  `genre` varchar(20) NOT NULL,
  `idDev` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `clients`
--

INSERT INTO `clients` (`id`, `nom`, `prenom`, `adresse`, `Telephone`, `genre`, `idDev`) VALUES
(2, 'kasereka', 'grace', 'butembo', '0992860217', 'masculin', 2),
(4, 'Kavira', 'Ludia', 'butembo', '0992897689', 'masculin', 2),
(5, 'kavira', 'mbuli', 'Butembo', '0971363184', 'masculin', 1),
(7, 'kavira', 'mbuli', 'Butembo', '0971363184', 'masculin', 1),
(8, 'kavira', 'mbuli', 'Butembo', '0971363184', 'masculin', 1),
(10, 'kasereka', 'grace', 'butembo', '0992860217', 'masculin', 2),
(11, 'kasereka', 'grace', 'butembo', '0992860217', 'masculin', 2),
(12, 'kasereka', 'grace', 'butembo', '0992860217', 'masculin', 2),
(13, 'kasereka', 'grace', 'butembo', '0992860217', 'masculin', 1),
(14, 'kasereka', 'grace', 'butembo', '0992860217', 'masculin', 1),
(15, 'Kakule', 'Ushindi', 'Butembo', '0995693290', 'masculin', 1),
(17, 'Kakule', 'Ushindi', 'bunia', '0995693290', 'masculin', 1),
(18, 'Kakule', 'Ushindi', 'bunia', '0995693290', 'masculin', 1),
(19, 'kavira ', 'lae', 'butembo', '09928602189', 'feminin', 1),
(20, 'kavira ', 'charli', 'butembo', '0995693290', 'feminin', 1),
(21, 'kakule', 'lus', 'butembo', '0992860210', 'masculin', 1),
(22, 'shangw', '', '', '', 'masculin', 1),
(23, 'kambale ', 'kule', 'Butembo', '0995693290', 'masculin', 1),
(24, 'louange ', 'kule', 'Butembo', '0995693290', 'feminin', 1);

-- --------------------------------------------------------

--
-- Structure de la table `devise`
--

CREATE TABLE `devise` (
  `id` int(11) NOT NULL,
  `description` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `devise`
--

INSERT INTO `devise` (`id`, `description`) VALUES
(1, 'USD'),
(4, 'CDF');

-- --------------------------------------------------------

--
-- Structure de la table `gestionnaires`
--

CREATE TABLE `gestionnaires` (
  `id` int(11) NOT NULL,
  `idTrans` int(11) NOT NULL,
  `Nom` varchar(100) NOT NULL,
  `Prenom` varchar(100) NOT NULL,
  `telephone` varchar(15) NOT NULL,
  `genre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `gestionnaires`
--

INSERT INTO `gestionnaires` (`id`, `idTrans`, `Nom`, `Prenom`, `telephone`, `genre`) VALUES
(5, 3, 'kavira ', 'louange ', '0993899878', 'masculin'),
(10, 1, 'lusenge', 'grace', '0992860217', 'masculin'),
(11, 1, 'kasereka', 'grace', '0992860217', 'masculin'),
(12, 2, 'kasereka ', 'Ushindi', '0995693290', 'masculin'),
(13, 20, 'kasereka', 'grace', '0992860217', 'masculin'),
(14, 2, 'gloria', 'vbasisia', '0971363184', 'masculin'),
(15, 1, 'kombi', 'indi', '0971363184', 'masculin');

-- --------------------------------------------------------

--
-- Structure de la table `rapports`
--

CREATE TABLE `rapports` (
  `id` int(11) NOT NULL,
  `idGestion` int(11) NOT NULL,
  `TypeRapport` varchar(100) NOT NULL,
  `DateDebut` date NOT NULL,
  `DateFin` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `rapports`
--

INSERT INTO `rapports` (`id`, `idGestion`, `TypeRapport`, `DateDebut`, `DateFin`) VALUES
(1, 1, 'journalier ', '2024-09-17', '2024-09-18'),
(3, 2, 'mensuel ', '2024-09-17', '2024-09-18'),
(4, 2, 'journalier ', '2024-10-03', '2024-10-03'),
(5, 12, 'mensuel ', '2024-10-06', '2024-10-06'),
(6, 12, 'journalier ', '2024-10-06', '2024-10-06'),
(7, 5, 'journalier ', '2024-10-06', '2024-10-06'),
(8, 14, 'mensuell', '2024-10-06', '2024-10-06');

-- --------------------------------------------------------

--
-- Structure de la table `transactions`
--

CREATE TABLE `transactions` (
  `id` int(11) NOT NULL,
  `idClient` int(11) NOT NULL,
  `Montant` decimal(10,0) NOT NULL,
  `DateTransaction` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `transactions`
--

INSERT INTO `transactions` (`id`, `idClient`, `Montant`, `DateTransaction`) VALUES
(1, 1, 20000, '2024-09-14'),
(2, 2, 20000, '2024-09-15'),
(6, 1, 7000, '2024-09-21'),
(14, 1, 29700, '2024-09-23'),
(15, 2, 120000, '2024-09-23'),
(16, 3, 5000, '2024-09-23'),
(17, 4, 70000, '2024-09-23'),
(18, 5, 4000, '2024-09-23'),
(19, 5, 4000, '2024-09-23'),
(20, 6, 78000, '2024-09-23'),
(21, 6, 4000, '2024-09-23'),
(22, 7, 500, '2024-09-23'),
(23, 8, 20000, '2024-09-23'),
(24, 6, 5500, '2024-09-23'),
(25, 1, 60000, '2024-09-25'),
(26, 2, 60000, '2024-09-25'),
(27, 5, 70000, '2024-08-25'),
(28, 4, 70000, '2024-09-25'),
(29, 2, 70000, '2024-09-27'),
(30, 3, 90000, '2024-09-27'),
(31, 1, 23900, '2024-09-27'),
(32, 1, 3000, '2024-09-27'),
(33, 1, 4000, '2024-10-04'),
(34, 2, 23900, '2024-10-04'),
(35, 17, 7000, '2024-10-05'),
(36, 2, 23900, '2024-10-11'),
(37, 2, 30, '2024-10-05'),
(38, 2, 4000, '2024-10-11'),
(39, 2, 7888888, '2024-10-05'),
(40, 4, 7888888, '2024-10-11'),
(41, 2, 60000, '2024-10-05'),
(42, 22, 40000, '2024-10-06');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idDev` (`idDev`);

--
-- Index pour la table `devise`
--
ALTER TABLE `devise`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `gestionnaires`
--
ALTER TABLE `gestionnaires`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idTrans` (`idTrans`);

--
-- Index pour la table `rapports`
--
ALTER TABLE `rapports`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idGestion` (`idGestion`);

--
-- Index pour la table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idClient` (`idClient`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `clients`
--
ALTER TABLE `clients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT pour la table `devise`
--
ALTER TABLE `devise`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `gestionnaires`
--
ALTER TABLE `gestionnaires`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT pour la table `rapports`
--
ALTER TABLE `rapports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pour la table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
