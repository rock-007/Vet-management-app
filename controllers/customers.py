from flask import Flask, Blueprint, redirect, render_template, request, url_for
from models.customer import Customer
from models.pet import Pet
import repositories.admin_repository as admin_repository
import repositories.customer_repository as customer_repository
import repositories.pet_repository as pet_repository
import pdb

customer_blueprint = Blueprint("customer", __name__)

#Check_the_admin_status
def check_admin():
    return admin_repository.get_status()


#customer_page_GET_Request 
@customer_blueprint.route("/customer", methods=["GET"])
def register_form():
    email = None

    if ( type(check_admin())!= str):
        return  redirect("/login")
    else:    
        email = check_admin()
        return render_template("customers/index.html", email=email)


#customer_page_POST_Request - SAVE
@customer_blueprint.route("/customer", methods=["POST"])
def register_customer():
    email = None
    if (type(check_admin()) is not str):
        return redirect("/login")
    else:    
        email = check_admin()
        customer = Customer(request.form['first_name'],request.form['last_name'], request.form['address'])
        customer_repository.register_customer(customer)
        pet = Pet(request.form['pet_name'],request.form['date_of_birth'], request.form['type'], customer)
        pet1 = pet_repository.register_pet(pet)
        print(pet1)
    return redirect("./appointments")
    

    
