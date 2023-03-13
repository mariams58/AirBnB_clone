#!/usr/bin/python3
""" defines the entry for the console """
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}



class HBNBCommand(cmd.Cmd):
    """ defines the console class """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ does not run the previous command if no command was entered """
        pass

    def do_create(self, args):
        """ Command to create a new instance of BaseModel """
        if not args:
            print("** class name missing **")
        elif args not in classes:
            print("** class name doesn't exist **")
        else:
            inst = BaseModel()
            inst.save()
            print(inst.id)

    def do_show(self, args):
        """Show command to print the string representation
        of an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) != 2:
                print("** instance id missing **")
            else:
                for key, value in storage.all().items():
                    if args[1] == value:
                        print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Destroy command to delete an inst based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) != 2:
                print("** instance id missing **")
            else:
                for key, value in storage.all().items():
                    if args[1] == value:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
