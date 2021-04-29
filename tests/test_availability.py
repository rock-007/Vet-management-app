from models.availability import Availability
from datetime import datetime, timedelta, time
import unittest

class TestAvailability(unittest.TestCase):



    def setUp(self):

        self.availability_1 = Availability()

    def test_availability_day_time(self):
        
        self.assertEqual(4,len(self.availability_1.day_time))


