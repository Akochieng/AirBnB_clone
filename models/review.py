#!/usr/bin/env python3
from models.base_model import BaseModel
'''representation of the reviews from users'''


class Review(BaseModel):
    '''updates reviews from users

    Attributes:
    place_id (str): the unique identifier of the place
    user_id (str): the id of the user
    text (str): the review from the user
    '''
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self):
        '''initialises a review instance using default values'''
        super().__init__()
