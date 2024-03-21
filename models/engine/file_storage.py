#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        obj = {}
        ''' validation '''
        if cls is None:
            return (self.__objects)
        else:
            new_obj = {obj: key for obj, key in self.__objects.items()}
                       if type(key) == cls}
            '''Return the new obj'''
        return (new)

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        vl_dict = obj
        FileStorage.__objects[key] = vl_dict

    def save(self):
        '''
            This serializes the __object attrib to JSON file
        '''
        objects_dict = {}
        for key, vl in FileStorage.__objects.items():
            objects_dict[key] = vl.to_dict()

        with open(FileStorage.__file_path, mode='w+' encoding='UTF8') as file1:
            json.dump(objects_dict, file1)

    def delete(self, obj=None):
        '''
            This public instance method deletes obj from __objects
        '''
        if not obj:
            return
        key = '{}.{}'.format(type(obj).__name, obj.id)
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()

    def reload(self):
        '''
            Deserializes the JSON file to the __objects
        '''
        try:
            with open(FileStorage.__file_path, encoding='UTF8') as file2:
                file_store = FileStorage.__objects
                file_store = json.load(file2)
                for key, vl in file_store.items():
                    clss_nm = vl['__class__']
                    clss_nm = models.classes[clss_nm]

                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
