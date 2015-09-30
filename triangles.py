def triangles():
	L = [1]
	yield L
	L = [1, 1]
	yield L
	while True:
		L = [1] + [L[i] + L[i+1] for i in range(len(L) - 1)] + [1]
		yield L

o = triangles()
n = 0
for t in o:
	print(t)
	n += 1
	if n == 10:
		break
