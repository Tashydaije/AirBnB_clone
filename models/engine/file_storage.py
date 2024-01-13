#!/usr/bin/python3
''' Filestorage class '''

import json
from models.base_model import BaseModel


class FileStorage:
    ''' Represents the storage engine '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns dictionary objects '''
        return FileStorage.__objects

    def new(self, obj):
        ''' Adds new obj to __objects with key '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__obects[key] = obj

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
                    self.new(eval(clsname)(**o))
        except FileNotFoundError:
            return

