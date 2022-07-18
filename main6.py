def next_val(n):
    i = 0
    string= ''
    while i <= n:
        string += str(i)
        i += 1
    print(int(string))


if __name__ == '__main__':
    n = int(input())
    next_val(n)