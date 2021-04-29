from db.run_sql import run_sql
from models.customer import Customer
import pdb
import repositories.customer_repository as customer_repository
from  models.pet import Pet


#register_pet
def register_pet(pet):
    sql= "INSERT INTO pets(name, type, contact_number, date_of_birth) VALUES(%s,%s, %s,%s) RETURNING id"
    values=[pet.pet_name, pet.type, pet.owner_contact, pet.date_of_birth]
    result = run_sql(sql,values)
    pet.id = result[0]['id']

    return pet

def search_pet_by_id(pet_id):
    sql = "SELECT * FROM pets WHERE  id = %s "
    values =[pet_id]
    result = run_sql(sql,values)[0]
    pet = Pet(result['name'],result['date_of_birth'],result['type'],result['contact_number'], pet_id)

    return pet

def delete_pet_by_id(pet_id):
    sql ="DELETE FROM pets WHERE id = %s"
    values=[pet_id]
    run_sql(sql,values)

def update_pet_details(pet):
    sql ="UPDATE pets SET (name, type, contact_number, date_of_birth) = (%s,%s,%s,%s) WHERE id = %s"
    values=[pet.pet_name, pet.type, pet.owner_contact, pet.date_of_birth, pet.id]
    pdb.set_trace()
    run_sql(sql,values)

def search_pet_by_name_date_of_birth(pet_name, pet_date_of_birth):
    sql = "SELECT * FROM pets WHERE  name = %s AND date_of_birth = %s"
    values=[pet_name, pet_date_of_birth]

    return run_sql(sql,values)[0]

def all_pets():
    sql = "SELECT * FROM pets"
    values=[]

    return run_sql(sql,values)



