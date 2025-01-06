def factorial(value):
    if value == 1:
        return value
    else:
        return value * factorial(value - 1)
    

# test
print(factorial(5))
print("---")


def countdown(value):
    if value <= 1:
        return value
    else:
        print(value)
        return countdown(value - 1)
    

# test
print(countdown(5))