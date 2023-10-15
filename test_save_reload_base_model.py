#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
'''
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model)
print("##################################################")
my_model.save()
print(my_model.to_dict())
'''
print("-- Create a new Place --")
my_place = Place()
my_place.name = "Muhuru Bay"
my_place.save()
print(my_place)

print("-- Create City --")
my_city = City()
my_city.name = "Mombasa"
my_city.save()
print(my_city)


print("-- Create a new State --")
my_state = State()
my_state.name = "Kenya"
my_state.save()
print(my_state)



print("-- Create a new Amenity --")
my_amenity = Amenity()
my_amenity.name = "Custom Inne"
my_amenity.save()
print(my_amenity)


print("-- Create a new Review --")
my_review = Review()
my_review.text = "This is crazy"
my_review.save()
print(my_review)
