if __name__ == '__main__':
    N = int(input())

    list_ = []
    for _ in range(N):
        params = input().split()
        if params[0] == 'append':
            list_.append(int(params[1]))
        elif params[0] == 'insert':
            list_.insert(int(params[1]),int(params[2]))
        elif params[0] == 'remove':
            list_.remove(int(params[1]))
        elif params[0] == 'sort':
            list_.sort()
        elif params[0] == 'reverse':
            list_.reverse()
        elif params[0] == 'pop':
            list_.pop()
        elif params[0] == 'print':
            print(list_)
        


