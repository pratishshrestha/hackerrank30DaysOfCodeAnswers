
S = [1,2,3,4,5,6,7,8]
K = 5
value = list()
result = list()
count = 8
while count > 0:
	A = S[count-1]
	for i in range(0,8):
		if A < S[i]:
			value.append(A & S[i])
	count -= 1
for i in range(0, len(value)):
	if value[i] < K:
		result.append(value[i])

print(max(result))

print(value)