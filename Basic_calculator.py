
def add(x,y):
    c = x+y
    return c

def sub(x,y):
    c = x - y
    return c

def division(x,y):
        c = x/y
        return c

def multiplication(x,y):
    c = x * y
    return c 

while True:
    a = float(input("enter the value of x : "))
    b = float(input("enter the value of y : "))
    print("1 : Addition")
    print("2 : Substraction")
    print("3 : Division")
    print("4 : Multiplication")

    choice = int(input("enter your choice"))


    if choice == 1:
        d = add(a,b)
        print("Your answer is--------------",d)

    if choice == 2:
        d = sub(a,b)
        print("Your answer is--------------",d)

    if choice == 3:
        if not b == 0:
            d = division(a,b)
            print("Your answer is--------------",d)
        else:
            print("incorrect value enterred")

    
    if choice == 4:
        d = multiplication(a,b)
        print("Your answer is--------------",d)


    print("your operation is completed here !")
    print("Let's do another one \n\n")