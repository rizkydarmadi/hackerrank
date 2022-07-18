y = [100,300,230,2,1,0]

# ambbil top three
y.sort(reverse=True)
z = []

for i in range(len(y)):
    x = {f'nama {i}':f'{y[i]}'}
    if i == 2:
        break
    z.append(x)

z.append({'lainya':str(sum(y[3:len(y)]))})
print(z)