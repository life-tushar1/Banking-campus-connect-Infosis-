-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 12, 2017 at 03:23 PM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bankM5`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_type`
--

CREATE TABLE `account_type` (
  `acc_type` varchar(10) NOT NULL,
  `min_balance` float DEFAULT NULL,
  `intrest%` int(10) DEFAULT NULL,
  `cust_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account_type`
--

INSERT INTO `account_type` (`acc_type`, `min_balance`, `intrest%`, `cust_id`) VALUES
('current', 9500, 7, 1),
('saving', 8500, 5, 2),
('saving', 10500, 5, 1),
('current', 7500, 5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `cust_info`
--

CREATE TABLE `cust_info` (
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `cust_id` int(10) NOT NULL,
  `Address` varchar(20) NOT NULL,
  `State` varchar(20) NOT NULL,
  `Pincode` int(10) NOT NULL,
  `City` varchar(20) NOT NULL,
  `Balance` float NOT NULL,
  `Transaction` varchar(10) NOT NULL,
  `Open_date` date NOT NULL,
  `Close_date` date DEFAULT NULL,
  `Block` varchar(5) DEFAULT NULL,
  `closed` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cust_info`
--

INSERT INTO `cust_info` (`first_name`, `last_name`, `cust_id`, `Address`, `State`, `Pincode`, `City`, `Balance`, `Transaction`, `Open_date`, `Close_date`, `Block`, `closed`) VALUES
('Tushar', 'Sharma', 1, 'villa no 31', 'uttrankand', 24891, 'delhi', 0, 'self', '2017-05-09', NULL, NULL, NULL),
('Swasti', 'kotyal', 2, 'race course', 'uttrankhand', 248001, 'dehradun', 0, 'self', '2017-05-10', NULL, NULL, NULL),
('megha', 'sigh', 3, 'villa 1', 'uttrakhand', 248001, 'dehradun', 0, 'self', '2017-05-12', '0000-00-00', 'null', 'nul');

-- --------------------------------------------------------

--
-- Table structure for table `fd`
--

CREATE TABLE `fd` (
  `acc_no` int(10) NOT NULL,
  `amount` int(10) NOT NULL,
  `duration` int(10) NOT NULL,
  `cust_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fd`
--

INSERT INTO `fd` (`acc_no`, `amount`, `duration`, `cust_id`) VALUES
(1, 1000, 16, 1),
(2, 2000, 13, 1),
(3, 5000, 13, 2);

-- --------------------------------------------------------

--
-- Table structure for table `loan`
--

CREATE TABLE `loan` (
  `loan_acc` int(10) NOT NULL,
  `loan_amt` float NOT NULL,
  `repay_term` date NOT NULL,
  `cust_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `loan`
--

INSERT INTO `loan` (`loan_acc`, `loan_amt`, `repay_term`, `cust_id`) VALUES
(1, 4000, '2017-06-10', 2),
(2, 200, '2017-08-19', 2),
(3, 9000, '2019-01-01', 1),
(4, 3000, '2019-09-01', 1),
(5, 2000, '2019-04-01', 1),
(6, 4000, '0000-00-00', 2);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `cust_id` int(10) NOT NULL,
  `password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`cust_id`, `password`) VALUES
(1, 'Tush91'),
(2, 'swas123'),
(3, 'megha12');

-- --------------------------------------------------------

--
-- Table structure for table `transact`
--

CREATE TABLE `transact` (
  `cust_id` int(10) NOT NULL,
  `acc_type` varchar(20) NOT NULL,
  `Date` date NOT NULL,
  `balance` float NOT NULL,
  `deposit` float NOT NULL,
  `widthdraw` float NOT NULL,
  `id_from` int(10) DEFAULT NULL,
  `id_to` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transact`
--

INSERT INTO `transact` (`cust_id`, `acc_type`, `Date`, `balance`, `deposit`, `widthdraw`, `id_from`, `id_to`) VALUES
(1, 'current', '2017-05-09', 5000, 5000, 0, NULL, NULL),
(2, 'saving', '2017-05-10', 5000, 5000, 0, NULL, NULL),
(1, 'saving', '2017-05-11', 5000, 5000, 0, NULL, NULL),
(2, 'current', '2017-05-11', 5000, 5000, 0, NULL, NULL),
(1, 'saving', '2017-05-11', 4000, 0, 500, NULL, NULL),
(1, 'saving', '2017-05-11', 3500, 0, 500, NULL, NULL),
(1, 'current', '2017-05-11', 5500, 0, 500, NULL, NULL),
(1, 'saving', '2017-05-11', 5500, 1000, 0, NULL, NULL),
(1, 'current', '2017-05-11', 8500, 3000, 0, NULL, NULL),
(1, 'saving', '2017-05-11', 5400, 0, 100, 1, 2),
(1, 'saving', '2017-05-11', 4400, 0, 1000, 1, 2),
(1, 'saving', '2017-05-11', 3400, 0, 1000, 1, 2),
(1, 'saving', '2017-05-11', 2400, 0, 1000, 1, 2),
(1, 'saving', '2017-05-11', 2300, 0, 100, 1, 2),
(2, 'saving', '2017-05-11', 2500, 100, 0, 1, 2),
(1, 'saving', '2017-05-11', 7500, 0, 1000, 1, 2),
(2, 'saving', '2017-05-11', 9500, 1000, 0, 1, 2),
(1, 'saving', '2017-05-11', 7500, 0, 1000, 1, 2),
(2, 'saving', '2017-05-11', 9500, 1000, 0, 1, 2),
(1, 'current', '2017-05-11', 6500, 0, 1000, 1, 2),
(2, 'current', '2017-05-11', 8500, 1000, 0, 1, 2),
(2, 'current', '2017-05-11', 7500, 0, 1000, 2, 1),
(1, 'current', '2017-05-11', 9500, 1000, 0, 2, 1),
(2, 'saving', '2017-05-11', 8500, 0, 1000, 2, 1),
(1, 'saving', '2017-05-11', 10500, 1000, 0, 2, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_type`
--
ALTER TABLE `account_type`
  ADD KEY `cust_id` (`cust_id`);

--
-- Indexes for table `cust_info`
--
ALTER TABLE `cust_info`
  ADD PRIMARY KEY (`cust_id`);

--
-- Indexes for table `fd`
--
ALTER TABLE `fd`
  ADD PRIMARY KEY (`acc_no`);

--
-- Indexes for table `loan`
--
ALTER TABLE `loan`
  ADD PRIMARY KEY (`loan_acc`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD UNIQUE KEY `cust_id` (`cust_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cust_info`
--
ALTER TABLE `cust_info`
  MODIFY `cust_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `fd`
--
ALTER TABLE `fd`
  MODIFY `acc_no` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `loan`
--
ALTER TABLE `loan`
  MODIFY `loan_acc` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `account_type`
--
ALTER TABLE `account_type`
  ADD CONSTRAINT `account_type_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `cust_info` (`cust_id`);

--
-- Constraints for table `login`
--
ALTER TABLE `login`
  ADD CONSTRAINT `login_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `cust_info` (`cust_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
