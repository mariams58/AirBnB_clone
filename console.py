#!/usr/bin/python3
""" defines the entry for the console """
import cmd


class HBNBCommand(cmd.Cmd):
    """ defines the console class """

    prompt = '(hbnb) '

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """Quit command to exit the program"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
