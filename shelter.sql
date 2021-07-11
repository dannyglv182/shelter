-- Dog Shelter Database
-- Postgres

/* Create database and connect */
DROP DATABASE shelter;
CREATE DATABASE shelter;
\c shelter;


/* Create tables */
CREATE TABLE food (
	food_id SERIAL PRIMARY KEY,
	name varchar(50),
	wet boolean,
	stock int
);


CREATE TABLE dog (
	dog_id SERIAL PRIMARY KEY,
	name text NOT NULL,
	arrival_date timestamp NOT NULL,
	adopted boolean,
	food_id int references food(food_id)
);


CREATE TABLE address (
	address_id SERIAL PRIMARY KEY,
	address varchar(50),
	city_id int,
	postal_code varchar(10)
);


CREATE TABLE adopter (
	adopter_id SERIAL PRIMARY KEY,
	first_name varchar(50),
	last_name varchar(50),
	email varchar(50) UNIQUE,
	address_id int references address(address_id)
);


CREATE TABLE city (
	city_id SERIAL PRIMARY KEY,
	city varchar(50),
	state varchar(3)
);


CREATE TABLE adopter_dog (
	adopter_id int references adopter (adopter_id) ON UPDATE CASCADE ON DELETE CASCADE,
	dog_id int references dog (dog_id) ON UPDATE CASCADE ON DELETE CASCADE,
	adoption_date timestamp NOT NULL,
	CONSTRAINT adopter_dog_pkey PRIMARY KEY (adopter_id, dog_id)
);
