/*
SQLyog Community v12.5.0 (64 bit)
MySQL - 10.1.29-MariaDB : Database - test
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`test` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `test`;

/*Table structure for table `_class` */

DROP TABLE IF EXISTS `_class`;

CREATE TABLE `_class` (
  `Id` char(38) NOT NULL,
  `Name` varchar(32) DEFAULT 'NULL',
  `Code` varchar(8) DEFAULT 'NULL',
  `Prerequisites` varchar(64) DEFAULT 'NULL',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `_class` */

/*Table structure for table `_classification` */

DROP TABLE IF EXISTS `_classification`;

CREATE TABLE `_classification` (
  `Id` char(38) NOT NULL,
  `Name` varchar(16) DEFAULT 'NULL',
  `Code` varchar(8) DEFAULT 'NULL',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `_classification` */

/*Table structure for table `_classmapping` */

DROP TABLE IF EXISTS `_classmapping`;

CREATE TABLE `_classmapping` (
  `Id` char(38) NOT NULL,
  `ClassId` char(38) NOT NULL,
  `Value` varchar(64) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `Class_Bit_Value` (`Value`),
  CONSTRAINT `Class_Bit_Value` FOREIGN KEY (`Value`) REFERENCES `_class` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `_classmapping` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
