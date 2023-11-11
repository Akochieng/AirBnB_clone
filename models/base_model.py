#!/usr/bin/env python3
import uuid
from datetime import datetime
from . import storage
'''
This module defines all the common methods for other classes
'''


class BaseModel():
    '''
    This class defines all the common methods for other classes
    in the web application

    id (str): unique identifier of an instance.
    created_at (str): time of creation of the object
    updated_at (str): when the instance was last updated
    '''
    def __init__(self, *args, **kwargs):
        '''
        Args:
            args: not implemented in the method
            kwargs: key word arguments of the method.
        '''
        if len(kwargs.keys()) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if (k != "__class__"):
                    setattr(self, k, v)

    def __str__(self):
        '''returns the string representation of the class'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''saves an instance of the class to the json storage'''
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        '''returns a dictionary representation of the object'''
        myval = self.__dict__.copy()
        created = myval.get('created_at')
        updated = myval.get('updated_at')
        myval.update({'created_at': created.isoformat()})
        myval.update({'updated_at': updated.isoformat()})
        myval.update({"__class__": self.__class__.__name__})
        return myval
