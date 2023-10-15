#!/usr/bin/env python3
from models.base_model import BaseModel
'''model representation of a city'''


class City(BaseModel):
    '''represents a city

    Attributes:
    state_id (str): unique identifier of a city. It will be the state.id
    name (str): the name of the city
    '''
    def __init__(self):
        '''initialises the city instance using default attr only'''
        super().__init__()
        self.state_id = ""
        self.name = ""
