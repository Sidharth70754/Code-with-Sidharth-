# function with **kwargs
# create a function that accepts any number of keyword arguments and prints them in the format key : value.

def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="sidharth", power="coding")
print_kwargs(name="sidharth")
print_kwargs(name="sidharth",power="coding",enemy="Dr.Jackaal")
