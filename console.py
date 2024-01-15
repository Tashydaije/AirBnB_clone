#!/usr/bin/python3
'''Console module'''
import cmd
from models.base_model import BaseModel
from shlex import split


class HBNBCommand(cmd.Cmd):
    '''Defines the command interpreter

    Attr:
        prompt (str): the command prompt
    '''
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
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
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        '''Prints the string repn of an instance based
        on the class name & id'''
        args = splits(arg)
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
        if key in BaseModel.__objects:
            print(BaseModel.__objectsl[key])
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
        if key in BaseModel.__objects:
            del BaseModel.__objects[key]
            BaseModel.save_to_file()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        '''Prints all string representation of all
        instances based or not on the class name.'''
        args = split(arg)
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        instance = []
        for key, value in BaseModel.__objects.items():
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
        if key not in BaseModel.__objects:
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
        instance = BaseModel.__objects[key]
        setattr(instance, attribute_name, attribute_value)
        instance.updated_at = datetime.now()
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()