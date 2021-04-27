from flask import Flask, Blueprint, redirect, render_template, request, url_for
from models.customer import Customer
from models.pet import Pet
# import repositories.admin_repository as admin_repository
import repositories.customer_repository as customer_repository
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

import pdb

appointment_blueprint = Blueprint("appointments", __name__)




# @appointment_blueprint.route("/appointments", methods=["GET"])
# def appointment_form():
#     result = []
#     return render_template('/appointments/index.html', result= result)


@appointment_blueprint.route("/appointments", methods=["GET"])
def book_appointment():
    #verify_customer\pet_details
    result = []
    # customer_id = customer_repository.search_id(request.form['customer_first_name'],request.form['customer_last_name'])
    # pet = pet_repository.search(request.form['pet_name'], customer_id)
    vets = vet_repository.select_vets()
    available_appointments = vet_repository.available_appointments(vets)
    # result.append(pet)
    # result.append(vets)
    result.append(available_appointments)
    pdb.set_trace()

    return render_template('/appointments/index.html', result=available_appointments)