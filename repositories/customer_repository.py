from db.run_sql import run_sql
from models.customer import Customer
import pdb

#register_customer
def register_customer(customer):
    #pdb.set_trace()
    sql= "INSERT INTO customers(first_name, last_name, address) VALUES(%s,%s,%s) RETURNING id"
    values=[customer.first_name,customer.last_name,customer.address]
    result = run_sql(sql,values)
    print (result)
    customer.id = result[0][0]
    return result

#Search_registered_users_id
def search_id(first_name, last_name):
    
    sql = "SELECT id FROM customers WHERE first_name=%s AND last_name=%s"
    values =[first_name, last_name]
    id = run_sql(sql,values)[0][0]
    # print("id")
    # print(id)
    # pdb.set_trace()
    return id

#Search_registered_users_
def search_customer(customer_id):
    
    sql = "SELECT * FROM customers WHERE id=%s"
    values =[customer_id]
    customer_info = run_sql(sql,values)[0]
    # print("id")
    # print(id)
    #pdb.set_trace()
    customer =Customer(customer_info['first_name'],customer_info['last_name'],customer_info['address'], customer_info['id'])

    return customer