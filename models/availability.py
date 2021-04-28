from datetime import datetime, timedelta, time

class Availability:
    def __init__(self):
        self.day_time = self.set_day_time()



    def set_day_time(self):
        day_time ={}
        todays_date = datetime.now().date()

        for delta in range(0,4):
            day_time[todays_date+timedelta(days=delta)] = [time(9,0), time(10,0), time(11,0), time(14,00), time(15,00)]
        return day_time


    def remove_slots(self, booked_slots):
        for each_day in self.day_time:
            for each_slot in booked_slots:
                if each_slot[0] == each_day:
                    self.day_time[each_day].remove(each_slot[1])