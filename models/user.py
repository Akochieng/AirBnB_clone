#!/usr/bin/env python3
from models.base_model import BaseModel
'''representation of users in the model'''


class User(BaseModel):
    '''models a typical user

    Attributes:
    first_name (str): the first name of the user
    last_name (str): the last name of the user
    email (str): the user's email
    password (str): the user's password
    '''
    first_name = ""
    last_name = ""
    email = ""
    password = ""
    def __init__(self):
        '''initialises a user instance using default arguments'''
        super().__init__()
