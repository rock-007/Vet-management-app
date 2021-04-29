from flask import Flask, Blueprint, redirect, render_template, request, url_for
from models.pet import Pet
from models.availability import Availability
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.appointment_repository as appointment_repository
import re
import pdb

appointment_blueprint = Blueprint("appointments", __name__)


@appointment_blueprint.route("/appointments", methods=["GET"])
def book_appointment_form():
    vets = vet_repository.select_vets()
    day_time_form = Availability()
    day_time_form.set_day_time()
    day_time_form_keys = day_time_form.day_time.keys()
    vets_availabilty = vet_repository.available_appointments(vets)
    
    all_appointments = appointment_repository.all_appointments()
    
    return render_template('/appointments/index.html', vets_availabilty=vets_availabilty, day_time_form_keys= day_time_form_keys, all_appointments= all_appointments )


@appointment_blueprint.route("/appointments", methods=["POST"])
def book_appointment():
    date_selected = request.form['date_selected']
    slot_selected = request.form['slot_selected']
    pet_name = request.form['pet_name']
    pet_date_of_birth = request.form['pet_date_of_birth']
    vet_id= request.form['vet_id']
    
    #book appointment
    result1 = appointment_repository.book_appoitment(date_selected, slot_selected, pet_name, pet_date_of_birth, vet_id)
    
    return redirect(url_for('appointments.book_appointment_form'))
