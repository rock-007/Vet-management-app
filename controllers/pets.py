from flask import Flask, Blueprint, redirect, render_template, request, url_for
from models.customer import Customer
from models.pet import Pet
import repositories.pet_repository as pet_repository
import pdb

pet_blueprint = Blueprint("pet", __name__)


#Create_Pet
@pet_blueprint.route("/add-pet", methods=["GET", "POST"])
def add_pet():
    
    if(request.method == 'POST'):
        pet_name = request.form['pet_name']
        date_of_birth = request.form['date_of_birth']
        pet_type = request.form['pet_type']
        pet = Pet(pet_name, date_of_birth, pet_type)
        result = pet_repository.register_pet(pet)
        # pdb.set_trace()
        print(result.id)
        return redirect(url_for('pet.pet_details', id=result.id))    
    else:
        return render_template('pets/new.html')

#Search_Pet_Info
@pet_blueprint.route("/pet/<id>", methods=["GET", "POST"])
def pet_details(id):
    pet = pet_repository.search_pet_by_id(id)
    return render_template('pets/index.html', pet = pet)

#Delete_Pet_Info
@pet_blueprint.route("/pet/<id>/delete", methods=["POST", "GET"])
def delete_pet_by_id(id):
    pet_repository.delete_pet_by_id(id)
    return redirect('/add-pet')

#Update_pet_info
@pet_blueprint.route("/pet/<id>/edit", methods=["POST", "GET"])
def update_pet_details(id):
    if(request.method == 'GET'):
        pet = pet_repository.search_pet_by_id(id)
        return render_template('pets/edit.html', pet = pet)
    else:
        pet_name = request.form['pet_name']
        date_of_birth = request.form['date_of_birth']
        pet_type = request.form['pet_type']
        pet_id = request.form['pet_id']
        pet = Pet(pet_name, date_of_birth, pet_type, pet_id)
        pet_repository.update_pet_details(pet)
        pdb.set_trace()
        return render_template('pets/index.html', pet = pet)
        
