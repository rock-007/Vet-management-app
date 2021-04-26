from db.run_sql import run_sql
from models.customer import Customer
import pdb
import repositories.customer_repository as customer_repository
from  models.pet import Pet


#register_customer
def register_pet(pet):
    sql= "INSERT INTO animals(name, date_of_birth, customer_id, type) VALUES(%s,%s,%s, %s) RETURNING id"
    values=[pet.name, pet.date_of_birth, pet.customer.id, pet.type]
    result = run_sql(sql,values)
    #pdb.set_trace()
    pet.id = result[0]['id']
    return pet


def search(pet_name, customer_id):
    pet = None
    sql = "SELECT * FROM animals WHERE customer_id = %s AND pet_name = %s "
    values =[customer_id,pet_name]
    result = run_sql(sql,values)[0]
    customer = customer_repository.search_customer(customer_id)
    pet = Pet(result['pet_name'],result['date_of_birth'],result['type'], customer,result['id'])

    #pdb.set_trace()



    return pet