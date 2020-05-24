import itertools
# define a list
my_list = [100,300,200,600,100,300,1000]

# get an iterator using iter()
myIter = iter(my_list)

print(myIter)

## iterate through it using next() 

#prints 100
print(next(myIter))

#prints 300
print(next(myIter))

## next(obj) is same as obj.__next__()

#prints 200
print(myIter.__next__())

#prints 600
print(myIter.__next__())

#prints 100
print(myIter.__next__())

#prints 300
print(myIter.__next__())


#prints 1000
print(myIter.__next__())


# ## This will raise error, no items left
# next(myIter)

for item in myIter:
    print(item)

