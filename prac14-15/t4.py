from t3 import *

# 4.1
true = K
false = KI
stringify = lambda x: x('Да')('Нет')

# 4.2
inv = C

# 4.3
if_then_else = I

# 4.4
either = K

# 4.5
both = lambda p: lambda q: p(q)(p)

# 4.6
eq = lambda p: lambda q: p(q)(inv(q))

# 4.7
Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))

# 4.8
Z = lambda g: (lambda x: g(lambda v: x(x)(v)))(lambda x: g(lambda v: x(x)(v)))
fact = Z(lambda f: lambda n: 1 if n==0  else  n * f(n-1))


if __name__ == '__main__':
    # 4.1
    # print(stringify(false))
    
    # 4.2
    # print(stringify(inv(false)))
    
    # 4.3
    # print(if_then_else(true)("Истина")("Ложь"))
    
    # 4.4
    # print(stringify(either(true)(false)), stringify(either(false)(false)))
   
    # 4.5
    # print(
    #     stringify(both(true)(true)), # Да
    #     stringify(both(false)(true)), # Нет
    #     stringify(both(true)(false)), # Нет
    #     stringify(both(false)(false)) # Нет
    # )
    
    # 4.6
    # print(
    #     stringify(eq(true)(true)), # Да
    #     stringify(eq(false)(true)), # Нет
    #     stringify(eq(true)(false)), # Нет
    #     stringify(eq(false)(false)) # Нет
    # )

    # 4.7
    # print(Y(lambda f: lambda n: 1 if n==0  else  n * f(n-1)))

    # 4.8
    print(fact(5))
