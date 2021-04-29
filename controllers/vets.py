from flask import Flask, Blueprint, redirect, render_template, request, url_for
from models.customer import Customer
from models.vet import Vet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

import pdb

vet_blueprint = Blueprint("vet", __name__)


#Create_Vet
@vet_blueprint.route("/add-vet", methods=["GET", "POST"])
def add_pet():
    
    if(request.method == 'POST'):
        vet_first_name = request.form['first_name']
        vet_last_name = request.form['last_name']
        vet_telephone_number = request.form['telephone_number']

        vet = Vet(vet_first_name, vet_last_name, vet_telephone_number)
        result = vet_repository.register_vet(vet)

        return redirect(url_for('vet.vet_details', id=result.id))    
    else:

        return render_template('vets/new.html')


#Search_Vet_Info
@vet_blueprint.route("/vet/<id>", methods=["GET", "POST"])
def vet_details(id):
    vet = vet_repository.search_vet_by_id(id)

    return render_template('vets/index.html', vet = vet)


#Delete_Vet_Info
@vet_blueprint.route("/vet/<id>/delete", methods=["POST", "GET"])
def delete_vet_by_id(id):
    vet_repository.delete_vet_by_id(id)

    return redirect('/add-vet')


#Update_pet_info
@vet_blueprint.route("/vet/<id>/edit", methods=["POST", "GET"])
def update_pet_details(id):

    if(request.method == 'GET'):
        vet = vet_repository.search_vet_by_id(id)

        return render_template('vets/edit.html', vet = vet)
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        telephone_number = request.form['telephone_number']
        vet_id = request.form['vet_id']
        
        vet = Vet(first_name, last_name, telephone_number, vet_id)
        vet_repository.update_vet_details(vet)

        return render_template('vets/index.html', vet = vet)
        