def even(i):
    return i ** 2

lst = [[str(i**2) for i in range(x*10-9, x*10+1)] for x in range(1, 11)]

chars = [len(x) for x in lst[-1]]
max_chars = sum(chars) # 41

for line in lst:
    print(*[item + " " * (chars[x] - len(item)) for x, item in enumerate(line)])
