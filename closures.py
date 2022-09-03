def outer_func(x):
    y = 4
    def inner_func(z): #this function will be returned and will be assigned to the variable closure
        print("inside inner_func")
        print(x + y + z)
        return x + y + z
    return inner_func

for i in range(3):
    print(i)
    closure = outer_func(i) # this is just defining the closure function
    print(closure(i + 5)) # here the closure function is actually called