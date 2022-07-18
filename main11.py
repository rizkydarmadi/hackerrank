if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

x = list(arr)
x.sort()

max_value = max(x)

for i in reversed(x):
    if i != max_value:
        print(i)
        break