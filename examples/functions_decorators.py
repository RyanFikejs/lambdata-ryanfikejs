"""Examples of weird function things and decorators"""


def say_hello(name):
    return f"hello {name}"


def be_cool(name):
    return f"Yo {name}, together we are cool!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


# if __name__ == "__main__"
#     greet_bob(say_hello)
#     greet_bob(be_cool)


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

def my_decorator(func):
    def wrapper():
            



# Decorator syntax

