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

        FileStorage.__filepath = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as f:
                dict_obj = json.load(f)
                for key, value in dict_obj.items():
                    class_ = key.split(".")[0]
                    if class_ in class_name:
                        FileStorage.__objects[key] = eval(class_)(**value)
                    else:
                        pass
