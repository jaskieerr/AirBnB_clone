#!/usr/bin/python3
'''File storage thingy'''
import json


class FileStorage:
    '''JSON serialization and deserialization'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects.'''
        return self.__objects

    def new(self, obj):
        '''Sets in __objects the obj with key.'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file (path: __file_path).'''
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()

        try:
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file)
        except Exception as e:
            print(f"Error saving file: {e}")

    def reload(self):
        '''Deserializes the JSON file to __objects.'''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            for key, obj_dict in data.items():
                class_name, obj_id = key.split('.')
                cls = globals()[class_name]
                obj = cls(**obj_dict)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
