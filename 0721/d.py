n, m = map(int,input().split())
data = []
for i in range(m):
	a, b = map(int, input().split())
	data.append([a, b])
data = sorted(data, key=lambda x: x[1])
p = -1
ans = 0
for a, b in data:
	if a <= p:
		continue
	else:
		p = b - 1
		ans += 1
print(ans)
