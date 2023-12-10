#!/usr/bin/python3
"""
Module for the console
"""

import cmd
from models.base_model import BaseModel
import json
import shlex
import re
import ast

class HBNBCommand(cmd.Cmd):
    """
    HBNbCommand interpretor
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_create(self, arg):
        """
        Function that create new instances
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instanse = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        function that show all information f an instance
        """
        My_commands = shlex.split(arg)
        if len(My_commands) == 0:
            print("** class name missing **")
        elif My_commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(My_commands) < 2:
            print("* instance id missing **")
        else:
            My_obj = storage.all()
            key = "{}.{}".format(My_commands[o], My_commands[1])
            if key in My_obj:
                print(My_obj[key])
            else:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """
        function to destroy an exicted instance
        """
        My_commands = shlex.split(arg)
        if len(My_commands) == 0:
            print("** class name missing **")
        elif My_commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(My_commands) < 2:
            print("* instance id missing **")
        else:
            My_obj = storage.all()
            key = "{}.{}".format(My_commands[o], My_commands[1])
            if key in My_obj:
                del(My_Obj[key])
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        """
        My_objects = storage.all()

        My_commands = shlex.split(arg)

        if len(My_commands) == 0:
            for key, value in My_objects.items():
                print(str(value))
        
        elif My_commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        
        else:
            for key, value in My_objects.items():
                if key.split('.')[0] == My_commands[0]:
                    print(str(value))

    def do_count(self, arg):
        """
        Counts the number of instances of a class
        """
        My_objects = storage.all()

        My_commands = shlex.split(arg)

        if arg:
            cls_num = My_commands[0]

        the_count = 0

        if My_commands:
            if cls_num in self.valid_classes:
                for obj in My_objects.values():
                    if obj.__class__.__name__ == cls_num:
                        the_count += 1
                print(the_count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")


    def do_update(self, arg):
        """
        Function to update the instances
        by adding or updating an attribute.
        """
        My_commands = shlex.split(arg)

        if len(My_commands) == 0:
            print("** class name missing **")
        elif My_commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(My_commands) < 2:
            print("** instance id missing **")
        else:
            My_objects = storage.all()

            key = "{}.{}".format(My_commands[0], My_commands[1])
            if key not in My_objects:
                print("** no instance found **")
            elif len(My_commands) < 3:
                print("** attribute name missing **")
            elif len(My_commands) < 4:
                print("** value missing **")
            else:
                obj = oMy_bjects[key]
                curved_races = re.search(r"\{(.*?)\}", arg)

                if curved_races:
                    try:
                        string_data = curved_races.group(1)

                        argu_dict = ast.literal_eval("{" + str_data + "}")

                        attribute_names = list(argu_dict.keys())
                        attribute_values = list(argu_dict.values())
                        try:
                            atr_name1 = attribute_names[0]
                            atr_value1 = attribute_values[0]
                            setattr(obj, atr_name1, atr_value1)
                        except Exception:
                            pass
                        try:
                            atr_name2 = attribute_names[1]
                            atr_value2 = attribute_values[1]
                            setattr(obj, atr_name2, atr_value2)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:

                    atr_name = My_commands[2]
                    atr_value = My_commands[3]

                    try:
                        atr_value = eval(atr_value)
                    except Exception:
                        pass
                    setattr(obj, atr_name, atr_value)

                obj.save()

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
