''' The service file interacts with the DB file to Query or Modify data within the database'''
# Typically there will be a function for each process that is required,
# and these will take in data and return data

import db
import sys
from os import *
import time

def get_all():
    '''shows all Records in database'''
    data = db.view_all_records()
    return data

def read_by_id(id):
    '''shows one employee which is specified by employee_id'''
    query = f'SELECT * FROM employees WHERE employee_id = {id};'
    data = db.run_query(query)
    return data

def create_record(forename, surname, email, job_title, num_phone_awards, city_location, manager_employee_id, currently_employed):
    '''Creates an employee in database'''
    query = f"INSERT INTO employees (forename, surname, email, job_title, num_phone_awards, city_location, manager_employee_id, currently_employed) VALUES ('{forename}', '{surname}', '{email}', '{job_title}', {num_phone_awards}, '{city_location}' {manager_employee_id}, '{currently_employed}');"
    db.run_query(query)
    return 'Record created'

def update_record(field, value, id):
    '''updates existing employee in database'''
    if isinstance(value, str):
        query = f"UPDATE employees SET {field} = '{value}' WHERE employee_id = {id};"
    else:
        query = f"UPDATE employees SET {field} = {value} WHERE employee_id = {id};"
    db.run_query(query)
    return 'Record updated'

def delete_record(id):
    '''deletes an employee which is specified by employee_id'''
    query = f'DELETE FROM employees WHERE employee_id = {id};'
    db.run_query(query)
    return 'Record deleted'

def delete_all():
    '''deletes all Records in database'''
    query = 'DELETE FROM employees WHERE employee_id > 0;'
    db.run_query(query)
    return 'All Records deleted'

def clear():
    '''function to clear the screen'''
	# for windows
    if name == "nt":
        _ = system("cls")
	# for mac and linux(here, os.name is "posix")
    else:
        _ = system("clear")
                
def animationscreen(text):
    '''function to create progress bar'''
    clear()
    print(text,"\n")
    for i in range(11):
        time.sleep(0.1)
        progress = "[ " + "■" * i + "□" * (10 - i) + " ]"
        sys.stdout.write("\033[F\033[K")  # Clear current line
        print(progress)
    clear()