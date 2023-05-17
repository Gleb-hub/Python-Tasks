# 1.2
def f(x):
    def power(y):
        return x ** y
    return power

# 1.3
f_2 = lambda x: lambda y: x ** y


if __name__ == '__main__':
    print(f_2(2)(3))
