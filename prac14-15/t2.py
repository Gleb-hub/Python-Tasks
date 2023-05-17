h = 10 ** -6

# 2.1
deriv = lambda func: lambda x: (func(x + h) - func(x)) / h

# 2.2
deriv_2 = lambda func: lambda x: (func(x + h) - func(x - h)) / (2*h)

if __name__ == '__main__':
    print(deriv_2(lambda x: x ** 3)(5))
