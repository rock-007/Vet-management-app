from flask import Flask, Blueprint, redirect, render_template, request
from models.customer import Customer
from models.pet import Pet

import repositories.admin_repository as admin_repository
import repositories.customer_repository as customer_repository
import repositories.pet_repository as pet_repository


login_blueprint = Blueprint("login", __name__)

#Check_the_admin_status
def check_admin():
    return admin_repository.get_status()


#customer_page
@login_blueprint.route("/customer", methods=["GET","POST"])
def customer():
    email = None
    if ( check_admin()!= str):
        redirect('/login')
        
    else:    
        email = check_admin()
        customer = Customer(request.form['first_name'],request.form['last_name'], request.form['address'])
        customer_repository.register_customer(customer)
        pet = Pet(request.form['name'],request.form['date_of_birth'], request.form['type'], customer)
        customer_repository.register_pet(pet)

    
    return render_template("customers/index.html", email=email)