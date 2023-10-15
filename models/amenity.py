#!/usr/bin/env python3
from models.base_model import BaseModel
'''representation of Amenities'''


class Amenity(BaseModel):
    '''model representing an amenity

    Attributes:
    name: string that loosely identifies an instance
    '''
    def __init__(self):
        super().__init__()
        '''initialises Amenity using base model default values'''
        self.name = ""
