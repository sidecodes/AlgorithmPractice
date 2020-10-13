def power(num, pwr):
    # breaking condition: if we reach zero
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(4, 5, power(4, 5)))
