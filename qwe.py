# 3.1
s = ['0', '1', '2', '3', '3']
print([int(i) for i in s])
print(list(map(int, s)))
# 3.2
s = ['0', '1', '2', '3', '3']
print(len(set(s)))
# 3.3
s = ['0', '1', '2', '3', '3']
print(s[::-1])
# 3.4
s = ['0', '1', '2', '3', '3']
x = '3'
print([ i for i, v in enumerate(s) if v == x])
# 3.5
s = [0, 1, 2, 3, 3]
print(sum([ v for i, v in enumerate(s) if i % 2 == 0]))
# 3.6
s = ['aaaaa', 'vvv', 'aca', 'qweqweqwe', 's']
print(max(s, key=lambda v: len(v)))
# 3.7
x = 333
print(not bool(x % sum(int(n) for n in str(x))))
# 3.8
print()




