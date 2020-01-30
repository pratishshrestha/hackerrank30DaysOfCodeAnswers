n = int(input())
myList = list()
for i in range(0,n):
	data = int(input())
	myList.append(data)

for j in range(0,n):
	if myList[j] > 1:
		for i in range(2,myList[j]):
			if (myList[j]%i) == 0:
				print("Not prime")
				break
		else:
			print("Prime")
	else:
		print("Not prime")