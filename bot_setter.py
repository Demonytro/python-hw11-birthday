from collections import UserDict
from datetime import datetime


def input_error(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Pls print: name and number'
        except TypeError:
            return 'Wrong command.'
    return wrapper


class AddressBook(UserDict):
    pass


class Record:
    pass


class Field:
    pass


class Name(Field):
    pass


class Phone(Field):
    pass


    
class Birthday(Field):
    pass


addressbook = AddressBook()


@input_error
def get_user_input():
    pass


@input_error
def get_handler(actions):
    return OPERATIONS[actions]


def hello_func(*args):
    print('How can I help you?')


@input_error
def add_func(user_input):
    pass


@input_error
def change_func(user_input):
    pass


@input_error
def phone_func(user_input):
    pass


@input_error
def delete_func(user_input):
    pass


@input_error
def remove_phone_func(user_input):
    pass


@input_error
def set_birthday(user_input):
    pass


@input_error
def show_birthday(user_input):
    pass


@input_error
def show_all_func(*args):
    pass


def break_func(*a):   
    pass


OPERATIONS = {
    'hello': hello_func,
    'add': add_func,
    'change': change_func,
    'phone': phone_func,
    'delete': delete_func,
    'remove': remove_phone_func,
    'set_birthday': set_birthday,
    'birthday': show_birthday,
    'show all': show_all_func,
    'good bye': break_func,
    'close': break_func,
    'exit': break_func
}


def main():
    pass


if __name__ == '__main__':
    main()