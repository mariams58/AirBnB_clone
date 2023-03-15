#!/usr/bin/python3
""" defines the FileStorage module """
import json
from os.path import exists
from models import base_model, user, review, place, state, city, amenity


BaseModel = base_model.BaseModel
User = user.User
Review = review.Review
Place = place.Place
State = state.State
City = city.City
Amenity = amenity.Amenity
name_class = ["BaseModel", "City", "State",
              "Place", "Amenity", "Review", "User"]


class FileStorage:
    """ serializes instances to a JSON file and
    deserializes JSON file to instances """

    __file_path = "file.json"

    __objects = {}

    def all(self):
        """ returns the instance method `__object`"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets the __objects key and value(obj) """
        name = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[name] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        dict_json = {}
        for key, value in FileStorage.__objects.items():
            dict_json[key] = value.to_dict()
        with open("file.json", "w", encoding="utf-8") as f:
            dump = json.dumps(dict_json)
            f.write(dump)

    def reload(self):
        """ deserializes the JSON file to __objects """
        dict_obj = {}

        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as f:
                dict_obj = json.load(f)
                for key, value in dict_obj.items():
                    class_ = key.split(".")[0]
                    if class_ in name_class:
                        FileStorage.__objects[key] = eval(class_)(**value)

                    else:
                        pass

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
