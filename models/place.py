#!/usr/bin/env python3
from models.base_model import BaseModel
'''representation of a place'''


class Place(BaseModel):
    '''model representation of a place

    Attributes:
    city_id (str): the id of the city
    user_id (str): the id of the user managing the place
    name (str): the name of the place
    description (str): description of the place
    number_rooms (int): number of rooms
    number_bathrooms (int): number of bathrooms
    max_guest (int): the number of guests
    price_by_night (int): the price
    latitude (float): the latitude
    longitude (float): the longitude
    amenity_ids (list): ids of amenities in the neighborhood
    '''
    def __init__(self):
        super().__init__()
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
