def even(i):
    return i ** 2


def main(N):
    lst = [[str(i ** 2) for i in range(x * 10 - 9, x * 10 + 1)] for x in range(1, N)]
    chars = [len(x) for x in lst[-1]]
    max_chars = sum(chars)
    for line in lst:
        print(*[item + " " * (chars[x] - len(item)) for x, item in enumerate(line)])

if __name__ == "__main__":
    N = int(input("Type a number of how many squares you want to see: "))
    main(N)





