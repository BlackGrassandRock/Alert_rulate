CREATE DATABASE rulate_bot;
use rulate_bot;
CREATE TABLE tlrulate (
Id VARCHAR(16),
Login VARCHAR(16) UNIQUE,
Password VARCHAR(32),
Stat_Answer VARCHAR(3),
Alert1 VARCHAR(500), Alert2 VARCHAR(500), Alert3 VARCHAR(500), Alert4 VARCHAR(500), Alert5 VARCHAR(500), 
Alert6 VARCHAR(500), Alert7 VARCHAR(500), Alert8 VARCHAR(500), Alert9 VARCHAR(500), Alert10 VARCHAR(500), 
Alert11 VARCHAR(500), Alert12 VARCHAR(500), Alert13 VARCHAR(500), Alert14 VARCHAR(500), Alert15 VARCHAR(500), 
Alert16 VARCHAR(500), Alert17 VARCHAR(500), Alert18 VARCHAR(500), Alert19 VARCHAR(500), Alert20 VARCHAR(500) 
);
ALTER TABLE `rulate_bot`.`tlrulate` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;