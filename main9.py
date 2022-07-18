if __name__ == '__main__':
    values = []
    all_data = []
    for _ in range(int(input())):
        store_data = []
        name = input()
        score = float(input())
        values.append(score)
        store_data.append(name)
        store_data.append(score)
        all_data.append(store_data)



from collections import Counter
same_value = [k for k,v in Counter(values).items() if v>1]

values.sort()

# get second lowest value
if len(same_value) > 1:
    same_value.sort()
    second_lowest_value = same_value[1]
else:
    second_lowest_value = list(dict.fromkeys(values))
    second_lowest_value = second_lowest_value[1]

result = []

for i in all_data:
    if i[1] == second_lowest_value:
        result.append(i[0])
result.sort()

for i in result:
    print(i)