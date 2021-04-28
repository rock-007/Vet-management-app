from flask import Flask, Blueprint, redirect, render_template, request, url_for
from models.customer import Customer
from models.pet import Pet
from models.availability import Availability
# import repositories.admin_repository as admin_repository
import repositories.customer_repository as customer_repository
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.appointment_repository as appointment_repository
import re
import pdb

appointment_blueprint = Blueprint("appointments", __name__)




# @appointment_blueprint.route("/appointments", methods=["GET"])
# def appointment_form():
#     result = []
#     return render_template('/appointments/index.html', result= result)


@appointment_blueprint.route("/appointments", methods=["GET"])
def book_appointment_form():
    #verify_customer\pet_details
    # result = []
    # customer_id = customer_repository.search_id(request.form['customer_first_name'],request.form['customer_last_name'])
    # pet = pet_repository.search(request.form['pet_name'], customer_id)

    vets = vet_repository.select_vets()
    day_time_form = Availability()
    day_time_form.set_day_time()
    day_time_form_keys = day_time_form.day_time.keys()
    vets_availabilty = vet_repository.available_appointments(vets)
    # result.append(pet)
    # result.append(vets)
    #result.append(vets_availabilty)
    #pdb.set_trace()

    return render_template('/appointments/index.html', vets_availabilty=vets_availabilty, day_time_form_keys= day_time_form_keys )

@appointment_blueprint.route("/appointments", methods=["POST"])
def book_appointment():
    date_selected = request.form['date_selected']
    slot_selected = request.form['slot_selected']
    pet_name = request.form['pet_name']
    pet_date_of_birth = request.form['pet_date_of_birth']
    
    #book appointment
    result1 = appointment_repository.book_appoitment(date_selected, slot_selected, pet_name, pet_date_of_birth)
    
    return render_template ('/index.html')
