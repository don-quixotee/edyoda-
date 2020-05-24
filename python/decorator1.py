def add_deco(func):
    def add_new(x,y):
        if type(x)==type(y):
          return func(x,y)
        else:
            return func(str(x),str(y))

    return add_new
@add_deco
def add(x,y):
    return x+y

print(add(10,100))
print(add('python', 'django'))
print(add(100, "react"))

