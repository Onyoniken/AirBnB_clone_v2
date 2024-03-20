#!/usr/bin/python3
"""imports from"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """class to test the place"""

    def __init__(self, *args, **kwargs):
        """class with __init__"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ city_test identification"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test user id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test_name fctn """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test descriptor"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test_number_rooms fctn"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test_number_bathrooms fctn"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test_max_guest fctn"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test_price_by_night fctn"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test_latitude fctn"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test_longitude fctn"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test_amenity_ids fctn"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
