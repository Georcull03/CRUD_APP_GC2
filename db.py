'''The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL'''

import sqlite3 as sql
from prettytable import from_db_cursor

conn = sql.connect('Employee-db')

cursor = conn.cursor()

def setup_table():
    '''sets up the database with a table created in opened file'''
    sql_file = open('Employees.sql')
    sql_string = sql_file.read()
    cursor.executescript(sql_string)

def run_query(query):
    '''allows interaction with database'''
    cursor.execute(query)
    data = from_db_cursor(cursor)
    return data

def view_all_records():
    '''shows all records in databse'''
    query = 'SELECT * FROM employees;'
    data = run_query(query)
    return data

def create_employee(forename, surname, email, job_title, num_phone_awards, city_location, manager_employee_id, currently_employed):
    '''creates an Employee'''
    query = f"INSERT INTO employees (forename, surname, email, job_title, num_phone_awards, manager_employee_id, currently_employed) VALUES ('{forename}', '{surname}', '{email}', '{job_title}', {num_phone_awards}, '{city_location}', {manager_employee_id}, '{currently_employed}');"
    run_query(query)
    return True

def commit_changes():
    '''saves changes to database'''
    conn.commit()


# setup_table()

# create_employee("Danny", "Lodge", "Dlogdge@corpemail.com", "Systems Developer", 52, 137, True)
# create_employee("Samuel", "Jenkins", "Sjenki@corpemail.com", "Support Engineer", 12, 437, True)
# print(view_all_records())

# conn.commit()