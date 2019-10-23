create database monitor;
use monitor;
create table pressure (v decimal(7,3), ts datetime primary key, IsNormal boolean,IsChecked boolean);
create table temperature1(v decimal(10,3),ts datetime primary key, IsNormal boolean,IsChecked boolean);
create table humidity(v decimal(10,3),ts datetime primary key,IsNormal boolean,IsChecked boolean);
create table locationx(v decimal(10,3),ts datetime primary key, IsNormal boolean,IsChecked boolean);
create table locationy(v decimal(10,3),ts datetime primary key, IsNormal boolean,IsChecked boolean);
create table vibration(v decimal(10,3),ts datetime primary key, IsNormal boolean,IsChecked boolean);
create table i(v decimal(10,3),ts datetime primary key, IsNormal boolean,IsChecked boolean);
create table u(v decimal(10,3),ts datetime primary key, IsNormal boolean,IsChecked boolean);
create table voice(v decimal(10,3),ts datetime primary key, IsNormal boolean,IsChecked boolean);

INSERT INTO `monitor`.`i` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('0.1', '2019:10:15 13:00', '1', '0');
INSERT INTO `monitor`.`i` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('0.1', '2019-10-15 13:01', '1', '0');

INSERT INTO `monitor`.`locationx` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('2', '2019-10-15 13:00:00', '1', '0');
INSERT INTO `monitor`.`locationx` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('3', '2019-10-15 13:01:00', '1', '0');
UPDATE `monitor`.`locationx` SET `ts` = '2019-10-23 10:29:00' WHERE (`ts` = '2019-10-15 13:00:00');
UPDATE `monitor`.`locationx` SET `ts` = '2019-10-23 10:29:01' WHERE (`ts` = '2019-10-15 13:01:00');
INSERT INTO `monitor`.`locationx` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('4', '2019-10-23 10:29:02', '1', '0');
INSERT INTO `monitor`.`locationx` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('5', '2019-10-23 10:29:03', '1', '0');
INSERT INTO `monitor`.`locationx` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('4', '2019-10-23 10:29:04', '1', '0');
INSERT INTO `monitor`.`locationx` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('3', '2019-10-23 10:29:05', '1', '0');



INSERT INTO `monitor`.`locationy` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('5', '2019-10-15 13:00:00', '1', '0');
INSERT INTO `monitor`.`locationy` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('4', '2019-10-15 13:00:10', '1', '0');
UPDATE `monitor`.`locationy` SET `ts` = '2019-10-23 10:29:00' WHERE (`ts` = '2019-10-15 13:00:00');
UPDATE `monitor`.`locationy` SET `ts` = '2019-10-23 10:29:01' WHERE (`ts` = '2019-10-15 13:01:00');
INSERT INTO `monitor`.`locationy` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('4', '2019-10-23 10:29:02', '1', '0');
INSERT INTO `monitor`.`locationy` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('5', '2019-10-23 10:29:03', '1', '0');
INSERT INTO `monitor`.`locationy` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('4', '2019-10-23 10:29:04', '1', '0');
INSERT INTO `monitor`.`locationy` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('3', '2019-10-23 10:29:05', '1', '0');



INSERT INTO `monitor`.`pressure` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('200', '2019-10-15 13:00:10', '1', '0');
INSERT INTO `monitor`.`pressure` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('200', '2019-10-15 13:01:10', '1', '0');

INSERT INTO `monitor`.`temperature1` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('22.3', '2019:10:15 13:00:00', '1', '0');
INSERT INTO `monitor`.`temperature1` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('22.2', '2019-10-15 13:00:01', '1', '0');

INSERT INTO `monitor`.`u` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('220', '2019-10-15 13:00:00', '1', '0');
INSERT INTO `monitor`.`u` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('220', '2019-10-15 13:00:01', '1', '0');

INSERT INTO `monitor`.`vibration` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('80', '2019-10-15 13:00:01', '1', '0');
INSERT INTO `monitor`.`vibration` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('80', '2019-10-15 13:00:02', '1', '0');

INSERT INTO `monitor`.`voice` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('80', '2019-10-15 13:00:01', '1', '0');
INSERT INTO `monitor`.`voice` (`v`, `ts`, `IsNormal`, `IsChecked`) VALUES ('90', '2019-10-15 13:00:02', '1', '0');
