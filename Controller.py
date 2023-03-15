'''The controller acts as the API for the app, in this case it will exist as a terminal based app'''
# using inputs and if statements to specify what the app should do

# It will run commands from the service file, which in turn uses the DB file to 
# query and create data and will return the data back to the user

from Service import *
import db

def start_app():

    # check if there are parameters provided, if not show the menu
    # if parameter is mode the skip menu and run that mode

    '''runs the app'''

    start_menu = """
    Welcome to the EH, what would you like to do with employe information? 
    1. Create a record
    2. Read a record by ID
    3. Read all records
    4. Update a record
    5. Delete a record
    6. Delete all records
    7. Exit
    """

    print(start_menu)
    exit = False

    # if (!param) then
    #     choice = int(input('kkkk'))
    # else if param > 0 && param < 7
    #     choice = param
    #     print('Running automatically with option ' + param)
    # else    
    #     error exit.....
    #     exit true
    

    while not exit:
        # choice = int(input('Please choose a mode to continue: '))
        choice = 3
        if choice == 1:
            animationscreen('Loading')
            print(create_records())
        elif choice == 2:
            animationscreen('Loading')
            print(read_id())
        elif choice == 3:
            animationscreen('Loading')
            print(read_all())
            exit = True
        elif choice == 4:
            animationscreen('Loading')
            print(update_a_record())
        elif choice == 5:
            animationscreen('Loading')
            print(delete_a_record())
        elif choice == 6:
            animationscreen('Loading')
            print(delete_records())
        else:
            animationscreen('Saving')
            exit = True
            db.commit_changes()
            print('Thanks for using EH!!')

def create_records():
    '''creates record in database'''
    forename = input('Please enter the employees first name: ')
    surname = input('Please enter the employees surname: ')
    email = input('Please enter the employees email: ')
    job_title = input('Please enter the employees job title: ')
    num_phone_awards = int(input('Please enter the number of phone tool awards owned by the employee: '))
    city_location = input('Please enter the location the employee is based: ')
    manager_employee_id = int(input('Please enter the manager ID of the employee: '))
    currently_employed = input('Please enter whether the employee has started employment: ')
    return create_record(forename, surname, email, job_title, num_phone_awards, city_location, manager_employee_id, currently_employed)

def read_all():
    '''reads all records in database'''
    return get_all()

def read_id():
    '''reads order which matches specified id in database'''
    id = input('Please enter a record id to read: ')
    return read_by_id(id)

def update_a_record():
    '''updates an order which matches specified id in database'''
    column = input('Please enter a column you would like to update: ')
    replacement_value = input('Please enter data to replace previous value: ')
    id = input('Please enter the record id you would like to update: ')
    return update_record(column, replacement_value, id)

def delete_a_record():
    '''deletes an order using specified id in database'''
    id = input('Please enter a record id to delete that record: ')
    return delete_record(id)

def delete_records():
    '''deletes all orders in database'''
    return delete_all()

# print(get_all())
start_app()