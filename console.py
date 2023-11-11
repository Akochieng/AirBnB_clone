#!/usr/bin/env python3
'''A commandline interface for the app

    This simple commandline application supports basic commands
    such as create, all, show, update and destroy which can be
    used to perform basic operations on the app backend.
'''
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    '''defines an object for the commandline interface of the web app

    Attributes:
    __valid_classes (list): list of the module's valid classes
    prompt: the object's prompt
    '''
    __valid_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                       "City": City, "Amenity": Amenity, "Place": Place,
                       "Review": Review}

    def __init__(self):
        '''initialises a commandline instance'''
        super().__init__()
        self.prompt = "(hbnh)"

    def emptyline(self):
        '''overwrites the default behaviour of the commandline for empty
        lines, does nothing instead'''
        pass

    def do_quit(self, args):
        '''Exits the commandline

        Usage: quit
        '''
        return True

    def do_EOF(self, args):
        '''Exits the commandline on receipt of the end of line character'''
        return True

    def cmdloop(self):
        '''Inherits from the commandline loop
        Terminates the loop when the keyboard interrupt is received
        Raises:
            KeyboardInterrupt

        '''
        try:
            super().cmdloop()
        except KeyboardInterrupt:
            return True

    def do_create(self, args):
        '''
        creates a new object of class args

        Usage: create <class name>
        '''
        if len(args) == 0:
            print("** class name missing **")
        elif args in HBNBCommand.__valid_classes.keys():
            cls = HBNBCommand.__valid_classes.get(args)
            new = cls()
            new.save()
            print(f"{new.id}")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        '''
        lists all the stored objects

        Args:
        args (str): the class name

        Usage: all
        Usage: all <class name>
        '''
        values = storage.all().values()
        if len(args) == 0:
            for val in values:
                print(val)
        elif args in HBNBCommand.__valid_classes:
            for val in values:
                if val.get("__class__") == args:
                    print(val)
        else:
            print("** class doesn't exist **")

    def get_obj(self, args):
        '''
        retrieves an object from the object list in storage

        Args:
        args: classname and id of the object

        Raises:
        ValueError: if the instance or class name is missing
        NameError: if the class name does not exist

        Return:
        Object representation of the retrieved object
        '''
        val = args.split()
        if len(val) == 0:
            raise ValueError("** class name missing **")
        elif len(val) == 2:
            cls, idy = val
            if cls in HBNBCommand.__valid_classes.keys():
                key = f"{cls}.{idy}"
                if key in storage.all().keys():
                    return key
            else:
                raise NameError("** class doesn't exist **")
        else:
            raise ValueError("** instance id missing **")

    def do_show(self, args):
        '''
        displays an instance

        Args:
        args: key identifier of the object in the storage
        '''
        try:
            obj = self.get_obj(args)
            if obj is None:
                print("** no instance found **")
            else:
                print(storage.all().get(obj))
        except (NameError, ValueError) as msg:
            print(msg)

    def do_update(self, args):
        '''
        updates the attributes of an instance

        args: the id of the object, the class, the attribute to be updated and
        its new value.
        '''
        val = args.split()
        if len(val) == 0:
            print("** class name missing **")
        else:
            try:
                key = self.get_obj(" ".join(val[:2]))
            except (ValueError, NameError) as msg:
                print(msg)
            else:
                if key is None:
                    print("** no instance found **")
                else:
                    obj = storage.all().get(key)
                    try:
                        attr = val[2]
                    except IndexError:
                        print("** attribute name missing **")
                    else:
                        try:
                            new_val = val[3]
                        except IndexError:
                            print("** value missing **")
                        else:
                            obj.update({attr: new_val})
                            storage.save()

    def do_destroy(self, args):
        '''
        deletes the specified instance

        Arguments:
        args: unique identifier of the instance
        '''
        try:
            key = self.get_obj(args)
        except (ValueError, NameError) as msg:
            print(msg)
        else:
            del storage.all()[key]
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
