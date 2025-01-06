def factorial(value):
    if value == 1:
        return value
    else:
        return value * factorial(value - 1)
    

# test
print(factorial(5))