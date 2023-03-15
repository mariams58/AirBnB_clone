#!/usr/bin/python3
""" Unittest case for the console """

with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
