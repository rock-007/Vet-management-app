from db.run_sql import run_sql
from models.customer import Customer

#register_customer
def register_pet(pet):
    sql= "INSERT INTO animals(name, date_of_birth, customer_id, type) WHERE VALUES(%s,%s,%s, %s) RETURNING id"
    values=[customer]
    result = run_sql(sql,values)[0]['id']
    customer.id = result
    return result