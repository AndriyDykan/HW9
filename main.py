

dict_of_known_numbers = dict()


def input_error(func):

    def inner(*args):

        try:
            return func(*args)
        except IndexError or ValueError or KeyError:
            return "wrong data. for help input 'help'"
    return inner


def show_all(*args):
    if dict_of_known_numbers:
        for key in dict_of_known_numbers:
            print(f"|{key}||{dict_of_known_numbers[key]}|")
        return "It`s your dict"
    else:
        return "you still don`t have any numbers in your dict"


@input_error
def phone(*args):
    data = args[0].split()
    if data[1].isdigit() and not dict_of_known_numbers.get(data[0]):
        dict_of_known_numbers[data[0]] = data[1]
        return "Data is in dict"
    raise IndexError


@input_error
def change(*args):
    data = args[0].split()
    if data[1].isdigit() and dict_of_known_numbers.get(data[0]):
        dict_of_known_numbers[data[0]] = data[1]
        return "data changed"
    raise IndexError


def hello(*args):
    return "How can I help you?"


def help(*args):
   return "phone - to add number\nchange - to change number\nexit - to exit\nshow all - to see dict"


def exit(*args):
    return "bye"


COMANDS = {exit: ("exit", "close", "good bye"),
           help: ("help",),
           change: ("change",),
           show_all: ("show all",),
           phone: ("phone",),
           hello: ("hello")}

print(COMANDS)
def undefind_comand(*args):
    return "I don`t know this command.Try help"


def input_normilize(data):
    for key, value in COMANDS.items():
        for i in value:
            if not data.find(i):
                comand = i
                return key, data.replace(comand, '').strip()
    return undefind_comand, None


def main():
    while True:
        user_input = input(">>>")
        command, data = input_normilize(user_input)
        print(command(data))
        if command == exit:
            break


if __name__ == "__main__":
    main()
