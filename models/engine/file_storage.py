#!/usr/bin/python3
""" defines the FileStorage module """
import json


class FileStorage:
    """ serializes instances to a JSON file and
    deserializes JSON file to instances """
    __file_path = "file.json"

    __objects = dict()

    def all(self):
        """ returns the instance method `__object`"""
        return self.__objects

    def new(self, obj):
        """ sets the __objects key and value(obj) """
        name = "{}.{}".format(type(obj).__name__, self.id)
        self.__objects[name] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path) as f:
                load = json.loads(f.read())
            self.__objects = {key: value for key, value in load.items())
        except FileNotFoundError:
            pass
