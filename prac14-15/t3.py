power = lambda x: lambda y: x ** y

# 3.1
I = lambda x: x
K = lambda x: lambda y: x
KI = lambda x: lambda y: y
C = lambda f: lambda x: lambda y: f(y)(x)
M = lambda x: x(x)

# 3.2
V = lambda a: lambda b: lambda f: f(a)(b)
pair = V
first = K
second = KI

if __name__ == '__main__': 
    # 3.1
    # print(I(42), # 42
    #       K(1)(2), # 1
    #       KI(1)(2), # 2
    #       C(power)(2)(5), # 25
    #       C(C(power))(2)(5), # 32
    #       M(lambda x: 42)) # 42
    
    # 3.2
    my_tuple = pair(3)(4)
    print(
        my_tuple(first),  # 3
        my_tuple(second) # 4
    )
