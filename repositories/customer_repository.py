from db.run_sql import run_sql
from models.customer import Customer

#register_customer
def register_customer(customer):
    sql= "INSERT INTO customers(first_name, last_name, address) WHERE VALUES(%s,%s,%s) RETURNING id"
    values=[customer]
    result = run_sql(sql,values)[0]['id']
    customer.id = result
    return result