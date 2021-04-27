from db.run_sql import run_sql
from models.customer import Customer
import pdb
import repositories.customer_repository as customer_repository
from  models.pet import Pet


#register_pet
def register_pet(pet):
    sql= "INSERT INTO pets(name, date_of_birth, type) VALUES(%s,%s,%s) RETURNING id"
    values=[pet.pet_name, pet.date_of_birth, pet.type]
    result = run_sql(sql,values)
    pdb.set_trace()
    pet.id = result[0]['id']
    return pet
# def register_pet(pet):
#     sql= "INSERT INTO animals(name, date_of_birth, customer_id, type) VALUES(%s,%s,%s, %s) RETURNING id"
#     values=[pet.name, pet.date_of_birth, pet.customer.id, pet.type]
#     result = run_sql(sql,values)
#     #pdb.set_trace()
#     pet.id = result[0]['id']
#     return pet
def search_pet_by_id(pet_id):
    sql = "SELECT * FROM pets WHERE  id = %s "
    values =[pet_id]
    result = run_sql(sql,values)[0]
    pet = Pet(result['name'],result['date_of_birth'],result['type'], pet_id)
    #pdb.set_trace()
    return pet

# def search(pet_name, customer_id):
#     pet = None
#     sql = "SELECT * FROM animals WHERE customer_id = %s AND pet_name = %s "
#     values =[customer_id,pet_name]
#     result = run_sql(sql,values)[0]
#     customer = customer_repository.search_customer(customer_id)
#     pet = Pet(result['pet_name'],result['date_of_birth'],result['type'], customer,result['id'])
#     #pdb.set_trace()
#     return pet

def delete_pet_by_id(pet_id):
    sql ="DELETE FROM pets WHERE id = %s"
    values=[pet_id]
    run_sql(sql,values)
    #pdb.set_trace()

def update_pet_details(pet):
    sql ="UPDATE pets SET(name, type, date_of_birth) =(%s, %s, %s) WHERE id = %s"
    values=[pet.pet_name, pet.type, pet.date_of_birth, pet.id]
    run_sql(sql,values)


def search_pet_by_name_date_of_birth(pet_name, pet_date_of_birth):
    sql = "SELECT * FROM pets WHERE  name = %s AND date_of_birth = %s"
    values=[pet_name, pet_date_of_birth]
    return run_sql(sql,values)[0]
    pdb.set_trace()

