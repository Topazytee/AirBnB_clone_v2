#!/usr/bin/python3
""" Console Module """
import cmd
import json
import shlex
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = ("(hbnb) ")

    def do_quit(self, args):
        """Quits the command"""
        return True

    def do_EOF(self, args):
        """Exit after receiving EOF signal"""
        return True

    def do_create(self, args):
        """ Create new instances an object of any class BaseModel"""
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            for i in args[1:]:
                try:
                    key = i.split("=")[0]
                    value = i.split("=")[1]
                    if hasattr(new_instance, key) is True:
                        value = value.replace("_", " ")
                        try:
                            value = eval(value)
                        except Exception:
                            pass
                        setattr(new_instance, key, value)
                except (ValueError, IndexError):
                    pass
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")
            return

    def do_show(self, args):
        """Print object representation of an instance"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_dict = storage.all(args[0])
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance based on class name and id"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        args = args.split(" ")
        obj_list = []
        objects = storage.all(args[0])
        try:
            if args[0] != "":
                models.classes[args[0]]
        except (KeyError, NameError):
            print("** class doesn't exist **")
            return
        try:
            for key, val in objects.items():
                obj_list.append(val)
        except Exception:
            pass
        print(obj_list)

    def do_update(self, args):
        """ Updates a certain object with new info """
        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()

    def emptyline(self):
        """Prevent printing when empty line is passed"""
        pass

    def do_count(self):
        """Counts and retrieves the instances"""
        obj_list = []
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(len(obj_list))

    def default(self):
        """Catch all unexplained named functions"""
        functions = {"all": self.do_all, "update": self.do_update, "show":
                     self.do_show, "count": self.do_count, "destroy":
                     self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".").replace('"', "").
                replace(",", "").split("."))
        try:
            cmd.arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)


if __name__ == "__main__":
    """Entry Point"""
    HBNBCommand().cmdloop()
