from models.pet import Pet
import unittest

class TestPet(unittest.TestCase):

    def setUp(self):

        self.pet_1 = Pet("Dolly","2021,04,02", "Cat")


    def test_pet_name(self):
        self.assertEqual("Dolly",self.pet_1.pet_name)