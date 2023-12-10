#!/usr/bin/python3
"""
Module for serializing and deserializing data
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
import os
import json

class FileStorage:
    """
    This class is for storing, serializing and deserializing data
    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """
         Sets an object in the __objects dictionary with a key of 
         <obj class name>.id.
        """
        obj_cls_names = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_names, obj.id)

        FileStorage.__objects[key] = obj


    def all(self):
        """
        Returns the __objects dictionary. 
        provides access to all the stored objects.
        """
        return  FileStorage.__objects


    def save(self):
        """
        Serializeing the __objects dictionary into 
        JSON format and saves it to the file specified by __file_path.
        """
        all_of_objs = FileStorage.__objects

        obj_dicts = {}

        for obj in all_of_objs.keys():
            obj_dicts[obj] = all_of_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as My_file:
            json.dump(obj_dicts, My_file)

    def reload(self):
        """
        This method is for deserializeing the JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as My_file:
                try:
                    obj_dicts = json.load(My_file)

                    for key, value in obj_dicts.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

if __name__ == '__main__':
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
