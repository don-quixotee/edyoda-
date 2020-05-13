import sys
print(sys.argv)


fp  = open("sys_err.txt", "w")
sys.stderr = fp
print(10/0)



print("holla!")

