-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 16, 2016 at 03:43 PM
-- Server version: 10.0.28-MariaDB-0ubuntu0.16.04.1
-- PHP Version: 7.0.8-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `serevrstatus`
--

-- --------------------------------------------------------

--
-- Table structure for table `statistiche`
--

CREATE TABLE `statistiche` (
  `ip` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `uptime` varchar(254) NOT NULL DEFAULT '0',
  `downtime` varchar(254) NOT NULL DEFAULT '0',
  `isUp` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `statistiche`
--

INSERT INTO `statistiche` (`ip`, `name`, `uptime`, `downtime`, `isUp`) VALUES
('162.244.29.55', 'developer3gs', '100', '0', 0),
('64.137.210.237', 'developer2git', '100', '0', 0),
('64.137.233.195', 'windows', '0', '50', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `statistiche`
--
ALTER TABLE `statistiche`
  ADD PRIMARY KEY (`ip`),
  ADD UNIQUE KEY `ip` (`ip`),
  ADD KEY `ip_2` (`ip`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
