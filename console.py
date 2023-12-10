#!/usr/bin/python3
"""
Module for the console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNbCommand interpretor
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quitting the command interpretor
        """
        return True

    def help_quit(self):
        """
        printing out what this command do
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        also quitting the command interpretor
        """
        return True

    def emptyline(self):
        """
        This function prevent repeating the previous
        commands when an empty line + ENTER
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
