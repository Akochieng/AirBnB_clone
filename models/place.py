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
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    def __init__(self):
        super().__init__()
