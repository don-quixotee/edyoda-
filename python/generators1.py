""" fibonacci number program using generators"""


def fibo():
    output = []
    num1 = 0
    yield num1

    num2 = 2
    yield num2

    while(True):
        next_num = num1 +num2
        yield next_num
        num1, num2 = num2, next_num


n = fibo()
print(next(n))
print(next(n))


# for x in n:

#     print()








