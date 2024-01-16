#!/usr/bin/python3
''' Filestorage class '''

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    ''' Represents the storage engine

    Attributes:
        __file_path (str): name of the file to save objects to
        __objects (dict): dictionary for objects storing
    '''
    __file_path = "file.json"
    __objects = {}
    _valid_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def all(self):
        ''' Returns dictionary objects '''
        return FileStorage.__objects

    def new(self, obj):
        ''' Adds new obj to __objects with key '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        ''' Serialize __objects to the JSON file __file_path '''
        objd = FileStorage.__objects
        objdict = {obj: objd[obj].to_dict() for obj in objd.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        ''' Deserialize the JSON file __file_path to __objects '''
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    clsname = o["__class__"]
                    del o["__class__"]
                    if clsname in self._valid_classes:
                        self.new(eval(clsname)(**o))
        except FileNotFoundError:
            return
