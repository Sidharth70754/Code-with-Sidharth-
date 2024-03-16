# example 1
username = "sidharth"

def func():
    username = "chai"
    print(username)

print(username)
func()

# example 2
x = 99
def fun2(y):
    z = x + y
    return z

result = fun2(1)
print(result)


# example 3
a = 100
def func3():
    global a
    a = 12
func3()
print(a)



# example 4
b = 99

def f1():
    b = 88
    def f2():
        print(b)
    f2()
f1()


def cahicoder(num):
    def actual(x):
        return x ** num
    return actual

f = cahicoder(2)
g = cahicoder(3)

print(f(3))
print(g(3))





















