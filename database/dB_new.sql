-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: blooddonationsystemdb
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_bloodbank`
--

DROP TABLE IF EXISTS `tbl_bloodbank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_bloodbank` (
  `idBloodbank` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idBloodbank`),
  UNIQUE KEY `idBloodbank_UNIQUE` (`idBloodbank`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_bloodbank`
--

LOCK TABLES `tbl_bloodbank` WRITE;
/*!40000 ALTER TABLE `tbl_bloodbank` DISABLE KEYS */;
INSERT INTO `tbl_bloodbank` VALUES (1,'Blood Delivery ','Blvd. 1 Decembrie 1918 nr.53','bloodDelivery@gmail.com','098802391'),(4,'Blood Bank North','Blvd. 2 Decembrie 1918 nr.53','bloodNorth@gmail.com','08923023134'),(5,'Blood Bank South','Blvd. 5 Decembrie 1918 nr.53','bloodSouth@gmail.com','0892301234');
/*!40000 ALTER TABLE `tbl_bloodbank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_bloodstock`
--

DROP TABLE IF EXISTS `tbl_bloodstock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_bloodstock` (
  `idBloodBag` int NOT NULL AUTO_INCREMENT,
  `idBloodBank` int NOT NULL,
  `bloodGroup` varchar(45) NOT NULL,
  `quantity` int NOT NULL,
  `expirationDate` date DEFAULT NULL,
  `donorId` int NOT NULL,
  PRIMARY KEY (`idBloodBag`),
  UNIQUE KEY `idBloodStock_UNIQUE` (`idBloodBag`),
  KEY `fk_BloodBank_idx` (`idBloodBank`),
  KEY `fk_DonorId_idx` (`donorId`),
  CONSTRAINT `fk_BloodBank` FOREIGN KEY (`idBloodBank`) REFERENCES `tbl_bloodbank` (`idBloodbank`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_DonorId` FOREIGN KEY (`donorId`) REFERENCES `tbl_donor` (`idDonor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_bloodstock`
--

LOCK TABLES `tbl_bloodstock` WRITE;
/*!40000 ALTER TABLE `tbl_bloodstock` DISABLE KEYS */;
INSERT INTO `tbl_bloodstock` VALUES (3,4,'AB-',2,'2222-02-22',1),(4,1,'A+',3,'2222-02-22',1),(5,1,'A+',21,'4444-02-21',1),(6,1,'A+',23,'3123-11-02',1),(7,1,'A+',1,'0000-00-00',1),(8,1,'0-',20,'2035-01-01',2);
/*!40000 ALTER TABLE `tbl_bloodstock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_donor`
--

DROP TABLE IF EXISTS `tbl_donor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_donor` (
  `idDonor` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  `date_of_birth` date NOT NULL,
  `location` varchar(45) NOT NULL,
  `bloodGroup` varchar(45) NOT NULL,
  `cnp` char(13) DEFAULT NULL,
  PRIMARY KEY (`idDonor`),
  UNIQUE KEY `idDonor_UNIQUE` (`idDonor`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_donor`
--

LOCK TABLES `tbl_donor` WRITE;
/*!40000 ALTER TABLE `tbl_donor` DISABLE KEYS */;
INSERT INTO `tbl_donor` VALUES (1,'Adi-Mihai','Neata','2222-12-12','Blvd. 1 Decembrie 1918 nr.53','AB-','21412234511'),(2,'Cristi','Darius','1890-12-22','Drumu Taberei nr 12','0-','2131231213213'),(4,'Radu','Alex','2001-02-22','Strada Arges 1','B+','32123213212'),(5,'Andrei','Catalin','2021-02-22','Strada Arges 1','0+','240021412412'),(6,'Radulescu','Andra','2000-10-17','Blvd. 1 Decembrie 1918 nr55','AB-','6085467389');
/*!40000 ALTER TABLE `tbl_donor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_request`
--

DROP TABLE IF EXISTS `tbl_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_request` (
  `idRequest` int NOT NULL AUTO_INCREMENT,
  `requestDate` date DEFAULT NULL,
  `idSeeker` int NOT NULL,
  `quantity` int DEFAULT NULL,
  `idBloodBank` int NOT NULL,
  `Approved` tinyint DEFAULT NULL,
  PRIMARY KEY (`idRequest`),
  UNIQUE KEY `idRequest_UNIQUE` (`idRequest`),
  KEY `fk_Seeker_idx` (`idSeeker`),
  KEY `fk_BloodBank_idx` (`idBloodBank`),
  KEY `fk_BloodBank_idx2` (`idBloodBank`),
  CONSTRAINT `fk_ReqBloodBank` FOREIGN KEY (`idBloodBank`) REFERENCES `tbl_bloodbank` (`idBloodbank`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Seeker` FOREIGN KEY (`idSeeker`) REFERENCES `tbl_seeker` (`idSeeker`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_request`
--

LOCK TABLES `tbl_request` WRITE;
/*!40000 ALTER TABLE `tbl_request` DISABLE KEYS */;
INSERT INTO `tbl_request` VALUES (3,'2018-02-18',3,3,1,0);
/*!40000 ALTER TABLE `tbl_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_seeker`
--

DROP TABLE IF EXISTS `tbl_seeker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_seeker` (
  `idSeeker` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  `date_of_birth` date NOT NULL,
  `location` varchar(45) NOT NULL,
  `blodGroup` varchar(45) NOT NULL,
  `cnp` char(13) DEFAULT NULL,
  PRIMARY KEY (`idSeeker`),
  UNIQUE KEY `idSeeker_UNIQUE` (`idSeeker`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_seeker`
--

LOCK TABLES `tbl_seeker` WRITE;
/*!40000 ALTER TABLE `tbl_seeker` DISABLE KEYS */;
INSERT INTO `tbl_seeker` VALUES (2,'Marius','Darius','2003-12-21','Drumu Taberei nr 12','B-','21341211114'),(3,'Radu','Dumitru','2002-02-22','Strada Arges 1','B+','21312321123'),(4,'Radulescu','Andra','2023-01-08','Blvd. 1 Decembrie 1918 nr55','AB+','5763176887899');
/*!40000 ALTER TABLE `tbl_seeker` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-09 22:53:59
