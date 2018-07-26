t = input()
result = []
hist = []
for i in range(int(t))
	data = input().split()
	a = int(data[0])
	b = int(data[1])
	c = int(data[2])
	d = int(data[3])
	hist.clear()
	while True
		if a  b
			result.append(No)
			break
		n = int((a  b))
		a -= b  n
		if a = c
			a += d
		if a in hist
			result.append(Yes)
			break
		else
			hist.append(a)
			if len(hist)  9000
				if min(hist)  a
					result.append(No)
					break
			if len(hist)  10000
				result.append(Yes)
				break
for i in range(int(t))
	print(result[i])
