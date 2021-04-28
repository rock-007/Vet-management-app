from db.run_sql import run_sql
import repositories.pet_repository as pet_repository

import pdb
def book_appoitment(date_selected, slot_selected, pet_name, pet_date_of_birth):
    #find pet id with pet name and date of birth
    pet = pet_repository.search_pet_by_name_date_of_birth(pet_name, pet_date_of_birth)

    sql ="INSERT INTO appointments(date, time, vet_id, pets_id) values(%s, %s, %s, %s) RETURNING id"
    values= [date_selected, slot_selected, 2, pet['id']]
    result = run_sql(sql,values)
    print(result)
    return print("tty")
