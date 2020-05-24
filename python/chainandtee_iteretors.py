import itertools

x = [100,200,300,400,500,600]
y = ["delhi", "Maumbai", "hydrabad","shimla"]
z = range(5,10)

i = itertools.chain(x,y,z)
t = itertools.tee(i,2)
print(t)
for value in t[0]:
    print(value)

for value in t:
    print(value)
print(type(t))

print(i)

