-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 07 oct. 2024 à 15:28
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
-- Base de données : `chat_app`
--

-- --------------------------------------------------------

--
-- Structure de la table `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `message` text NOT NULL,
  `sent_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `messages`
--

INSERT INTO `messages` (`id`, `sender_id`, `receiver_id`, `message`, `sent_at`) VALUES
(3, 11, 12, 'Bonjour!', '2024-08-21 10:35:52'),
(4, 11, 12, 'Bonjour! comment tu vas?', '2024-08-21 11:59:42'),
(5, 13, 11, 'Bonjour!', '2024-08-21 12:05:36'),
(6, 11, 13, 'Bonjour ca va?', '2024-08-21 12:06:15'),
(7, 12, 28, 'Bonjour!', '2024-10-05 12:48:54');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `profile_picture` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `firstname`, `lastname`, `profile_picture`) VALUES
(11, 'Glory', '$2y$10$zZhSAkGti12Sw1C5ozp68u0.XF7QAYqPnw8foBdBSrs9cgq5GwToi', 'Glory', 'Ind', 'images/img-11.JPG'),
(12, 'Blessing', '$2y$10$zA2VYOhlun2kmSGUGmC4e.R9eN/UcZ0AcJHPuLvJyCLjt/FQyMkiK', 'Blessing', 'Basisia', 'images/img-12.JPG'),
(13, 'Mwisa', '$2y$10$8FnW/bY6jrQ053cjHZuW..8QFXAKYdaCJ1KMHd1JFUPcXQ8LvD8te', 'Mwisa', 'Basisia', 'images/img-13.JPG'),
(26, 'Plame2', '$2b$12$ApkPHf9vXKwDxcO7XSW3huDWDvsnM4SUL6kz9ns9R5DKPv6PtL2Iq', 'Muyisa', 'Basisia', 'image'),
(27, 'MK', '$2b$12$Q7gsgsMFQheBjtQYwa94ce3mgXIdS7Kw/I1Ff3fNsEmX0bShiemIe', 'Muyisa', 'Kavalami', 'image'),
(28, 'suzy', '$2b$12$.6SXRz7eJpAqK3Tu8mNhqOVzcCHrV.ez3D6TYdLv5iFphxwMukd9i', 'suzan', 'mbah', 'image'),
(29, 'jamas', '$2b$12$.k4pqxquM64G8mglA5radui0B2IMrsNxTVBggbmLA8KkJAtHilOlu', 'janvier', 'masi', 'image'),
(32, 'Plame Bs', '$2b$12$3FRxmfnAyetPWGcmvXfrJO/1C5XfMq2HW7.QCrKMAvoWyM6jSoR1C', 'Plame', 'Basisia', 'image'),
(37, 'Exau', '$2b$12$5JcHTjBFKrlR3upIL2QiBO5AAq3d9VdT9NGxix5j49VamzJI7Hfji', 'Exauce', 'kav', 'image'),
(38, 'Bonheur', '$2b$12$JEXPeMfBMe8OLddCKOFYdesONMfyppjTlatjw.jxIzAoDlAFSdage', 'Muyisa', 'katusi', 'image');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sender_id` (`sender_id`),
  ADD KEY `receiver_id` (`receiver_id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `messages`
--
ALTER TABLE `messages`
  ADD CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`receiver_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
