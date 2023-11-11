#!/usr/bin/env python3
import json
'''manages  the json files for the module'''


class FileStorage():
    '''
    Defines methods for managing json file storage for the model

    Attributes:
    __file_path: the path to the file
    __objects: dictionary with all the objects created
    '''
    def __init__(self):
        '''initialises the class'''

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        '''returns a dictionary representation of all the objects
        saved'''
        return self.__objects

    def new(self, obj):
        '''adds an object to the list of objects stored

        Args:
            thekey: the key used in the dictionary of all objects
            obj: the object to be added to the list
        '''
        thekey = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects.update({thekey: obj.to_dict()})

    def save(self):
        '''saves the objects to a json file'''
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        '''loads objects from the json file'''
        try:
            with open(self.__file_path) as f:
                decoded = json.load(f)
                if decoded is not None:
                    self.__objects = decoded
        except FileNotFoundError:
            pass
