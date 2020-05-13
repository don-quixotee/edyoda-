import sys
print(sys.argv)


# num1= int(sys.argv[1])
# num2 = int(sys.argv[2])


fp  = open("sys_output.txt", "w")
sys.stdout = fp



print("holla!")

