#!/usr/bin/python3
'''comman interpreter'''
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''Command interpreter class.'''

    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit the program.'''
        return True

    def do_EOF(self, arg):
        '''EOF command to exit the program.'''
        print()
        return True

    def emptyline(self):
        '''Do nothing on empty line.'''
        pass

    def do_create(self, arg):
        '''Creates  new instance of BaseModel'''
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        '''shows str representation of instances'''
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''TADDMIIIIRRR HAHAHAHA'''
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        '''prints alll'''
        args = arg.split()
        objects = storage.all()
        result = []
        if not args:
            for obj_key in objects:
                result.append(str(objects[obj_key]))
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        else:
            for obj_key in objects:
                if obj_key.split('.')[0] == args[0]:
                    result.append(str(objects[obj_key]))
        print(result)

    def do_update(self, arg):
        '''updates instances based on class name n id.'''
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                instance = objects[key]
                setattr(instance, args[2], eval(args[3]))
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
