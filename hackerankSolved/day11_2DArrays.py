arr = []
maxHourGlass = 0
row = 6
column = 6
for i in range(0, row):
    temp_row = []
    for j in range (0, column):
        temp_row.append(int(input()))
    #print(temp_row)
    arr.append(temp_row)
    #print(arr)
#print(arr)


for i in range(0, row - 2):
	for j in range(0, column - 2):
		sumHourGlass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
		maxHourGlass = max(sumHourGlass, maxHourGlass)

print(maxHourGlass)