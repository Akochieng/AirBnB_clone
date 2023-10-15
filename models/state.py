#!/usr/bin/env python3
from models.base_model import BaseModel
'''representation of states in the model'''


class State(BaseModel):
    '''Representation of states in the model

    Attributes:

    name (str): the name of the state
    '''
    def __init__(self):
        '''Initialises the states model'''
        super().__init__()
        self.name = ""
