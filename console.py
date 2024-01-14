#!/usr/bin/python
'''Console module'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''Defines the command interpreter

    Attr:
        prompt (str): the command prompt
    '''
    prompt = "(hbnb) "

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

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()