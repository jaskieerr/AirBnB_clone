#!/usr/bin/python3
'''File storage thingy'''
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''JSON serialization and deserialization'''
    __file_path: str = "file.json"
    __objects: dict = dict()

    def all(self):
        '''Returns the dictionary __objects.'''
        return self.__objects

    def new(self, obj):
        '''Sets in __objects the obj with key.'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file (path: __file_path).'''
        temvar1: dict = {k: v.to_dict() for k, v in self.__objects.items()}

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(temvar1, f)

    def destroy(self, key):
        '''Deserializes the JSON file to __objects.'''
        try:
            del self.__objects[key]

            self.save()
            return True
        except KeyError:
            return False

    def reload(self):
        '''Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised).
        '''

        __model_classes = {"BaseModel": BaseModel,
                           "User": User,
                           "Place": Place,
                           "State": State,
                           "City": City,
                           "Amenity": Amenity,
                           "Review": Review}
        tempvar2: dict = {}
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                tempvar2 = json.loads(f.read())
            for key, value in tempvar2.items():
                sckey = key.split(".")[0]
                if sckey in __model_classes.keys():
                    self.__objects[key] = __model_classes[sckey](**value)
        except (KeyError, FileNotFoundError):
            pass
