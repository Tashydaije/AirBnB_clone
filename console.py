#!/usr/bin/python3
'''Console module'''
import cmd
from models.base_model import BaseModel
from shlex import split
from models import storage
from models.engine.file_storage import FileStorage
from models import base_model
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''Defines the command interpreter

    Attr:
        prompt (str): the command prompt
    '''
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        '''Quit command to exit program'''
        return True
    
    def do_EOF(self, arg):
        '''EOF signal to exit program'''
        print("")
        return True

    def emptyline(self):
        '''Do nothing on emptyline'''
        pass

    def do_create(self, arg):
        '''creates new instance of BaseModel, saves it
        to json file and prints id'''
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = getattr(base_model, class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        '''Prints the string repn of an instance based
        on the class name & id'''
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        ''' Deletes an instance based on the class name and id n saved'''
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        '''Prints all string representation of all
        instances based or not on the class name.'''
        args = split(arg)
        instance = storage.all()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        instances = []
        for key, value in instance.items():
            if not args or args[0] == value.__class__.__name__:
                instances.append(str(value))
        print(instances)

    def do_update(self, arg):
        '''Updates an instance based on the class name and
        id by adding or updating attribute (save into JSON file).'''
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.updated_at = datetime.now()
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
