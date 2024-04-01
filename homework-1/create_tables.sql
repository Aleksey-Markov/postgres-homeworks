-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id serial PRIMARY KEY,
	first_name varchar(15) NOT NULL,
	last_name varchar(15) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date date NOT NULL,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(5) UNIQUE NOT NULL,
	company_name varchar(30) NOT NULL,
	contact_name varchar(30) NOT NULL
);

CREATE TABLE orders
(
	order_id smallint NOT NULL,
	customer_id varchar(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id smallint REFERENCES employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(30)
);