if __name__ == '__main__':
	x = int(input())
	y = int(input())
	z = int(input())
	n = int(input())

d = []

for i in range(x+1):
	for j in range(y+1):
		for k in range(z+1):
			d.append([i,j,k])

print(d)

