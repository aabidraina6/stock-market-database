drop database if exists stock_db;
create database stock_db;
use stock_db;

CREATE TABLE if not EXISTS `User` (
  `AccountID` int AUTO_INCREMENT,
  `Name` varchar(500),
  `Contact` varchar(15),
  `Email` varchar(500),
  `Location` varchar(500),
  `Password` varchar(500),
  `PAN_Info` varchar(500),
  PRIMARY KEY (`AccountID`),
  CONSTRAINT password_should_be_more_than_8_characters CHECK (LENGTH(`Password`) >= 8)
);

CREATE TABLE if not EXISTS `Ticker` (
  `TickerID` int AUTO_INCREMENT,
  `Date` Date,
  `Open_Price` float,
  `High_Price` float,
  `Closing_Price` float,
  `Adjusted_Closing_Price` float,
  `Volume` int,
  `Company_Symbol` varchar(500),
  PRIMARY KEY (`TickerID`)
);

CREATE TABLE if not EXISTS `Company` (
  `CompanyID` int AUTO_INCREMENT,
  `Name` varchar(500),
  `Owner` varchar(500),
  `StockID` int,
  `Symbol` varchar(500),
  `Industry` varchar(500),
  `Sector` varchar(500),
  PRIMARY KEY (`CompanyID`)
);

CREATE TABLE if not EXISTS `Currency` (
  `Code` char(3),
  `Name` varchar(500),
  `IsActive` bool,
  `Region` varchar(500),
  `Exchange_Rate` float,
  PRIMARY KEY (`Code`)
);

CREATE TABLE if not EXISTS `holdings` (
  `TransactionID` int PRIMARY KEY AUTO_INCREMENT,
  `No_of_Shares_bought` int,
  `Total_Price` float
);

CREATE TABLE if not EXISTS `Broker` (
  `Name` varchar(500),
  `License_Number` int AUTO_INCREMENT,
  `Brokerage_Fee` float,
  PRIMARY KEY (`License_Number`)
);

CREATE TABLE if not EXISTS `Dependents` (
  `Name` varchar(500),
  `DependentID` int PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE if not EXISTS `Sector` (
  `Name` varchar(500),
  `Industry` varchar(500),
  PRIMARY KEY (`Name`)
);

CREATE TABLE if not EXISTS `company_stocks` (
  `CompanyID` int,
  `StockID` int,
  `Name` varchar(500)
);

CREATE TABLE if not EXISTS `user_has_dependents` (
  `UserID` int,
  `DependentID` int
);

CREATE TABLE if not EXISTS `brokerage` (
  `UserID` int,
  `Broker_License_Number` int
);

CREATE TABLE if not EXISTS `provides_holding` (
  `UserID` int,
  `CompanyID` int,
  `HoldingTransactionID` int
);

CREATE TABLE if not EXISTS `holding_value` (
  `HoldingTransactionID` int,
  `TickerID` int
);

CREATE TABLE if not EXISTS `currency_value` (
  `CurrencyCode` char(3),
  `TickerID` int
);

CREATE TABLE if not EXISTS `company_sector` (
  `CompanyID` int,
  `SectorName` varchar(500)
);

ALTER TABLE `Company` ADD FOREIGN KEY (`StockID`) REFERENCES `company_stocks` (`StockID`);

ALTER TABLE `user_has_dependents` ADD FOREIGN KEY (`UserID`) REFERENCES `User` (`AccountID`);

ALTER TABLE `user_has_dependents` ADD FOREIGN KEY (`DependentID`) REFERENCES `Dependents` (`DependentID`);

ALTER TABLE `brokerage` ADD FOREIGN KEY (`UserID`) REFERENCES `User` (`AccountID`);

ALTER TABLE `brokerage` ADD FOREIGN KEY (`Broker_License_Number`) REFERENCES `Broker` (`License_Number`);

ALTER TABLE `provides_holding` ADD FOREIGN KEY (`UserID`) REFERENCES `User` (`AccountID`);

ALTER TABLE `provides_holding` ADD FOREIGN KEY (`CompanyID`) REFERENCES `Company` (`CompanyID`);

ALTER TABLE `provides_holding` ADD FOREIGN KEY (`HoldingTransactionID`) REFERENCES `holdings` (`TransactionID`);

ALTER TABLE `holding_value` ADD FOREIGN KEY (`HoldingTransactionID`) REFERENCES `holdings` (`TransactionID`);

ALTER TABLE `holding_value` ADD FOREIGN KEY (`TickerID`) REFERENCES `Ticker` (`TickerID`);

ALTER TABLE `currency_value` ADD FOREIGN KEY (`CurrencyCode`) REFERENCES `Currency` (`Code`);

ALTER TABLE `currency_value` ADD FOREIGN KEY (`TickerID`) REFERENCES `Ticker` (`TickerID`);

ALTER TABLE `company_sector` ADD FOREIGN KEY (`CompanyID`) REFERENCES `Company` (`CompanyID`);

ALTER TABLE `company_sector` ADD FOREIGN KEY (`SectorName`) REFERENCES `Sector` (`Name`);

ALTER TABLE `company_stocks` ADD FOREIGN KEY (`CompanyID`) REFERENCES `Company` (`CompanyID`);

INSERT INTO `User` (`AccountID`, `Name`, `Contact`, `Email`, `Location`, `Password`, `PAN_Info`) VALUES
(1, 'Root', '9999999999', 'root@root.com', 'India', 'rootroot', '1234567890');
