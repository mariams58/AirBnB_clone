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
            print("** class doesn't exist **")
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

    def do_all(self, args):
        """ Prints all str reprsentn of all instances
        based on class name or not """
        args = args.split()
        if len(args) > 0 and arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            strl = []
            for item in storage.all().values():
                if len(args) > 0 and arg[0] == item.__class__.__name__:
                    strl.append(item.__str__())
                elif len(args) == 0:
                    strl.append(item.__str__())
            print(strl)

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).Usage
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". """
        args = args.split()
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in storage.all().keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) > 3:
            obj = storage.all()["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    value_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = value_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()
    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = args.split()
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
