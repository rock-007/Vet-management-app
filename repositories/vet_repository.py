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
    index_1 = 0
    index_2 = 0
    index_3 = 0
    todays_date = datetime.now().date()
    #setting 5-NextDates as keys for availablity
    




    # each vet below
    while index_2 < len(vets):
        temp =Availability()

        while index_1 < 5:
            temp.day_time[todays_date+timedelta(days=index_1)] = [time(9,0), time(10,0), time(11,0)]
            index_1 += 1
        
        sql= "SELECT date,time FROM appointments WHERE vet_id = %s AND date > %s AND date < %s "
        values = [vets[index_2].id, todays_date, todays_date + timedelta(days=5)]
        booked_slots = run_sql(sql, values)

        while index_3 < 5:
            for each_slot in booked_slots:
                if each_slot[0] == todays_date+timedelta(days=index_3):
                    print(index_2)
                    print(each_slot[1])
                    print("xxx")
                    print(temp.day_time[todays_date+timedelta(days=index_3)].remove(each_slot[1]))
            index_3 += 1
        vets[index_2].availability = temp.day_time
        index_2 += 1
    pdb.set_trace()

    return vets

