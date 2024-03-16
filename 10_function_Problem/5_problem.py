# default parameter value 
# write a function that greets a user. if no name is provided , it should greet with a default name.

def greet(name = "user"):
    return "hello," + name + "!"

print(greet("chai"))
print(greet())
