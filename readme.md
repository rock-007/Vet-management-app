# Vet_Management_App

This App is designed for the Vet Hospital, where it can manage the day to day activity with the customers. Particular usefull for the person at the front desk e.g Receptionist.

#  App_Functionality

The app can perform the below functionality

- Register Pet/Vet
- Search Pet/Vet
- Delete Pet/Vet
- Book Appointments


#  Installation_Instructions

First you need to install Python and Flask,it has been tested on python `2.7.16` and Flask `1.1.2` with no issues. Also need to install `psycopg library`. The easy way is using brew that will take care of the installation and any associated packages but for flask and psycopg we can use `pip` that will come with pre activated environment so no need to set environment separately.

- `$ brew install python3`
- `$ pip install Flask`
- `$ pip install psycopg2-binary`


In the end we also need to install the `psql` database ion local machine

- `brew install postgresql`



#  Structure


.
├── __pycache__
│   └── app.cpython-39.pyc
├── app.py
├── console.py
├── controllers
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── appointments.cpython-39.pyc
│   │   ├── customers.cpython-39.pyc
│   │   ├── login.cpython-39.pyc
│   │   ├── pets.cpython-39.pyc
│   │   └── vets.cpython-39.pyc
│   ├── appointments.py
│   ├── customers.py
│   ├── login.py
│   ├── pets.py
│   └── vets.py
├── db
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   └── run_sql.cpython-39.pyc
│   ├── run_sql.py
│   └── vet_management_new.sql
├── models
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── availability.cpython-39.pyc
│   │   ├── customer.cpython-39.pyc
│   │   ├── pet.cpython-39.pyc
│   │   └── vet.cpython-39.pyc
│   ├── availability.py
│   ├── customer.py
│   ├── pet.py
│   └── vet.py
├── readme.md
├── repositories
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── admin_repository.cpython-39.pyc
│   │   ├── appointment_repository.cpython-39.pyc
│   │   ├── customer_repository.cpython-39.pyc
│   │   ├── pet_repository.cpython-39.pyc
│   │   └── vet_repository.cpython-39.pyc
│   ├── admin_repository.py
│   ├── appointment_repository.py
│   ├── customer_repository.py
│   ├── pet_repository.py
│   └── vet_repository.py
├── run_tests.py
├── static
│   └── css
│       ├── form.css
│       └── style.css
├── templates
│   ├── appointments
│   │   └── index.html
│   ├── base.html
│   ├── customers
│   │   ├── base.html
│   │   └── index.html
│   ├── index.html
│   ├── login_page
│   │   ├── base.html
│   │   └── index.html
│   ├── pets
│   │   ├── base.html
│   │   ├── edit.html
│   │   ├── index.html
│   │   ├── new.html
│   │   └── search.html
│   └── vets
│       ├── edit.html
│       ├── index.html
│       └── new.html
└── tests
    ├── __pycache__
    │   ├── test_availability.cpython-39.pyc
    │   ├── test_pet.cpython-39.pyc
    │   └── test_vet.cpython-39.pyc
    ├── test_availability.py
    └── test_pet.py



# Local_preview

Home page will be available by default at  http://localhost:5050