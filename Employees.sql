CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    email VARCHAR(35),
    job_title VARCHAR(30),
    num_phone_awards INTEGER,
    city_location VARCHAR(20),
    manager_employee_id INTEGER,
    currently_employed BOOLEAN NOT NULL
);

INSERT INTO employees (forename, surname, email, job_title, num_phone_awards, manager_employee_id, currently_employed) VALUES ('Jerry', 'Smith', 'Jsmith@corpemail.com', 'support engineer', 17, 298, 'False');
INSERT INTO employees (forename, surname, email, job_title, num_phone_awards, city_location, manager_employee_id, currently_employed) VALUES ('Rebecca', 'Watts', 'Rwatts@corpemail.com', 'systems engineer', 27, 'Beijing', 242, 'True');