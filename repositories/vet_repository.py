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
    temp = []




    # each vet below
    while index_2 < len(vets):
        print(index_2)
        
        temp.append(Availability(vets[index_2].id))

        while index_1 < 5:
            temp[index_2].day_time[todays_date+timedelta(days=index_1)] = [time(9,0), time(10,0), time(11,0)]
            index_1 += 1
        
        sql= "SELECT date,time,vet_id FROM appointments WHERE vet_id = %s AND date > %s AND date < %s"
        values = [vets[index_2].id, todays_date, todays_date + timedelta(days=5)]
        booked_slots = run_sql(sql, values)
        

        while index_3 < 5:
            for each_slot in booked_slots:
                if each_slot[0] == todays_date+timedelta(days=index_3):
                    print(index_2)
                    print(each_slot['time'])
                    print("xxx")
                    print(temp[index_2].day_time[todays_date+timedelta(days=index_3)].remove(each_slot[1]))
            index_3 += 1
        pdb.set_trace()
        vets[index_2].availability = temp[index_2].day_time    
        index_2 += 1
        

    return vets

