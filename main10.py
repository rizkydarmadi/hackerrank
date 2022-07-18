nested_list = [['blue', 'brown'], ['red', 'brown'], ['blue', 'white']]
for inner in nested_list:
    for value in inner:
        if value == 'brown':
            print(value)
        # if value[1]=='brown':
        #     print(value[0])
        

