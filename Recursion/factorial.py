def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num-1)


print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(10, factorial(10)))
