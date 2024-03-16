# function with *args 
# write a function that takes variable of arguments and return their sum 

def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1,2,3))
