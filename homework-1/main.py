"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv
import psycopg2

with psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="83436891"
) as conn:
    with conn.cursor() as cur_emp:
        with open('north_data/employees_data.csv', 'r', encoding='utf=8') as file:
            header = next(file)
            rows = csv.reader(file)
            for row in rows:
                query = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)"
                cur_emp.execute(query, row)

    with conn.cursor() as cur_cust:
        with open('north_data/customers_data.csv', 'r', encoding='utf=8') as file:
            header = next(file)
            rows = csv.reader(file)
            for row in rows:
                query = "INSERT INTO customers VALUES (%s, %s, %s)"
                cur_cust.execute(query, row)

    with conn.cursor() as cur_order:
        with open('north_data/orders_data.csv', 'r', encoding='utf=8') as file:
            header = next(file)
            rows = csv.reader(file)
            for row in rows:
                query = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)"
                cur_order.execute(query, row)

conn.close()
