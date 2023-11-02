-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 16, 2023 at 08:25 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

-- Database: `odontofeedback`


-- Table structure for table `feedback`

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `nome` varchar(30) DEFAULT NULL,
  `nascimento` date DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `consultas` int(3) DEFAULT NULL,
  `tratamentos` varchar(30) DEFAULT NULL,
  `notaAtendimento` varchar(10) DEFAULT NULL,
  `notaTratamento` varchar(10) DEFAULT NULL,
  `dentista` varchar(13) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Dumping data for table `feedback`

INSERT INTO `feedback` (`id`, `nome`, `nascimento`, `sexo`, `consultas`,`notaAtendimento`,`notaTratamento`,`dentista`,`tratamentos`) VALUES
('0', 'Emily', '1999-12-09', 'F', 5, 9, 8, 'Udo'),
('1', 'Ana', '2000-02-10', 'F', 4, 10, 8, 'Sabrina'),
('2', 'Amanda', '2000-08-11', 'F', 1, 5, 8, 'Larissa'),
('3', 'julia', '2000-02-06', 'F', 2, 10, 8, 'Gladson'),
('4', 'Luiza', '1980-08-01', 'F', 4, 5, 10, 'André'),
('5', 'Gabrielle', '1980-02-02', 'F', 1, 5, 10, 'André'),
('6', 'Bianca', '1980-04-11', 'F', 1, 10, 10, 'Sabrina'),
('7', 'Ana Clara', '2001-02-04', 'F', 1, 10, 10, 'Sabrina'),
('8', 'Theodore', '2001-04-02', 'M', 3, 10, 9, 'Gustavo'),
('9', 'Guilherme', '2001-11-11', 'M', 2, 10, 9, 'Gustavo'),
('10', 'Victor', '1998-08-20', 'M', 5, 5, 5, 'Gladson'),
('11', 'Hugo', '1998-11-30', 'M', 4, 5, 5, 'Udo'),
('12', 'Mauricio', '1996-08-24', 'M', 10, 8, 10, 'Larissa'),
('13', 'José', '1996-04-17', 'M', 8, 7, 2, 'Udo'),
('14', 'Bruno', '2008-04-09', 'M', 9, 7, 10, 'Sabrina');

-- Indexes for table `feedback`

ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

-- AUTO_INCREMENT for table `feedback`

ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1001;
COMMIT;