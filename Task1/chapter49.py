#global Variable
x = 100

def fun(x):
    #local scope of variable
    x = 3 + 2
    return x

local = fun(x)
print(local)
print(x)