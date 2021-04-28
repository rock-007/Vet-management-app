from datetime import datetime, timedelta, time
from db.run_sql import run_sql
from models.vet import Vet
from models.availability import Availability
import pdb


def select_vets():
    result = run_sql('SELECT * FROM vets')
    vet = []
    for row in result:
        each_vet = Vet(row['first_name'], row['last_name'], row['telephone_number'], row['id'] )
        vet.append(each_vet)
    return vet




def available_appointments(vets):
    todays_date = datetime.now().date()
    #setting 5-NextDates as keys for availablity
    # each vet below
    for vet in vets:
        vet.availability =Availability()

        sql= "SELECT date,time FROM appointments WHERE vet_id = %s AND date > %s AND date < %s OR date =%s"
        values = [vet.id, todays_date, todays_date + timedelta(days=5), todays_date]
        booked_slots = run_sql(sql, values)
        
        vet.availability.remove_slots(booked_slots)
        #pdb.set_trace()        
    return vets

#Create_vet
def register_vet(vet):
    sql= "INSERT INTO vets(first_name, last_name, telephone_number) VALUES(%s,%s,%s) RETURNING id"
    values=[vet.first_name, vet.last_name, vet.telephone_number]
    result = run_sql(sql,values)
    #pdb.set_trace()
    vet.id = result[0]['id']
    return vet

#Search_by_id
def search_vet_by_id(vet_id):
    sql = "SELECT * FROM vets WHERE  id = %s "
    values =[vet_id]
    result = run_sql(sql,values)[0]
    vet = Vet(result['first_name'],result['last_name'],result['telephone_number'], vet_id)
    #pdb.set_trace()
    return vet

#Delete_by_id
def delete_vet_by_id(vet_id):
    sql ="DELETE FROM vets WHERE id = %s"
    values=[vet_id]
    run_sql(sql,values)
    #pdb.set_trace()


#Update_Vet_details
def update_vet_details(vet):
    sql ="UPDATE vets SET(first_name, last_name, telephone_number) =(%s, %s, %s) WHERE id = %s"
    values=[vet.first_name, vet.last_name, vet.telephone_number, vet.id]
    run_sql(sql,values)
    #pdb.set_trace()

