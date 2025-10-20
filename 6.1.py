import math


def performOperation(*args, operation='sum'):
    if operation == 'sum':
        return sum(args)
    if operation == 'multiply':
        return math.prod(args)
print(f"({performOperation(1, 2, 3, 6, 7, 8, operation='sum')})")