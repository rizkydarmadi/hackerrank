if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    x = student_marks[str(query_name)]

    result = sum(x)/len(x)
    print(format(result,'.2f'))