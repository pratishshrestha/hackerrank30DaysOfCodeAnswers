#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
counter = 0
# Write Your Code Here
while True:
	sort = -1 
	for i in range(0,n-1): #n-1 because it goes out of range for eg, n = 2 , a= [2,1] then a[1] > a[2]; a[2] is out of index
		if a[i] > a[i+1]:
			a[i], a[i+1] = a[i+1], a[i] #swap shortcut in python
			sort = i
			counter += 1
	if sort == -1:
		break
print("Array is sorted in " + str(counter) + " swaps.")
print("First Element: "  + str(a[0]))
print("Last Element: " + str(a[n-1]))