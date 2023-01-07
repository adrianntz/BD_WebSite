-- /#############################################################/
/*        PARTEA 1 - STERGEREA SI RECREAREA BAZEI DE DATE      */

DROP DATABASE blooddonationsystemdb;
CREATE DATABASE blooddonationsystemdb;

USE blooddonationsystemdb;

-- /#############################################################/




-- /#############################################################/
/*                  PARTEA 2 - CREAREA TABELELOR              */

CREATE TABLE  tbl_bloodbank  (
   idBloodbank  INT(11) NOT NULL AUTO_INCREMENT,
   name  VARCHAR(45) NULL DEFAULT NULL,
   address  VARCHAR(255) NOT NULL,
   email  VARCHAR(45) NULL DEFAULT NULL,
   phone_number  VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY ( idBloodbank ));

CREATE TABLE  tbl_donor  (
   idDonor  INT(11) NOT NULL AUTO_INCREMENT,
   firstName  VARCHAR(45) NULL DEFAULT NULL,
   lastName  VARCHAR(45) NULL DEFAULT NULL,
   date_of_birth  DATE NOT NULL,
   location  VARCHAR(45) NOT NULL,
   bloodGroup  VARCHAR(45) NOT NULL,
   cnp  CHAR(13) NULL DEFAULT NULL,
  PRIMARY KEY ( idDonor ));

CREATE TABLE  tbl_bloodstock  (
   idBloodBag  INT(11) NOT NULL AUTO_INCREMENT,
   idBloodBank  INT(11) NOT NULL,
   bloodGroup  VARCHAR(45) NOT NULL,
   quantity  INT(11) NOT NULL,
   expirationDate  DATE NULL DEFAULT NULL,
   donorId  INT(11) NOT NULL,
  PRIMARY KEY ( idBloodBag ),
  CONSTRAINT  fk_BloodBank 
    FOREIGN KEY ( idBloodBank )
    REFERENCES  tbl_bloodbank  ( idBloodbank )
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT  fk_DonorId 
    FOREIGN KEY ( donorId )
    REFERENCES  tbl_donor  ( idDonor )
    ON DELETE CASCADE
    ON UPDATE CASCADE);

CREATE TABLE  tbl_seeker  (
   idSeeker  INT(10) NOT NULL,
   firstName  VARCHAR(45) NULL DEFAULT NULL,
   lastName  VARCHAR(45) NULL DEFAULT NULL,
   date_of_birth  DATE NOT NULL,
   location  VARCHAR(45) NOT NULL,
   blodGroup  VARCHAR(45) NOT NULL,
   cnp  CHAR(13) NULL DEFAULT NULL,
  PRIMARY KEY ( idSeeker ));

CREATE TABLE  tbl_request  (
   idRequest  INT(11) NOT NULL AUTO_INCREMENT,
   requestDate  DATE NULL DEFAULT NULL,
   idSeeker  INT(11) NOT NULL,
   quantity  INT(11) NULL DEFAULT NULL,
   idBloodBank  INT(11) NOT NULL,
   Approved  TINYINT(4) NULL DEFAULT NULL,
  PRIMARY KEY ( idRequest ),
  CONSTRAINT  fk_ReqBloodBank 
    FOREIGN KEY ( idBloodBank )
    REFERENCES  tbl_bloodbank  ( idBloodbank )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT  fk_Seeker 
    FOREIGN KEY ( idSeeker )
    REFERENCES  tbl_seeker  ( idSeeker )
    ON DELETE CASCADE
    ON UPDATE CASCADE);

/#############################################################/




/#############################################################/
/*         PARTEA 3 - INSERAREA INREGISTRARILOR IN TABELE      */


/#############################################################/



/#############################################################/
/*  PARTEA 4 - VIZUALIZAREA STUCTURII BD SI A INREGISTRARILOR  */
DESCRIBE tbl_seeker;
DESCRIBE tbl_donor;
DESCRIBE tbl_bloodbank;
DESCRIBE tbl_bloodstock;
DESCRIBE tbl_request;
/#############################################################/

