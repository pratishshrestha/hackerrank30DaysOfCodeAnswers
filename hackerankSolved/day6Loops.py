

def checkUserInput():
	while True:
		global userInput 
		userInput = input()
		if len(userInput) < 2 or len(userInput) > 10000:
		    print("Please enter length of the string between 2 and 10000")
		    continue
		else:
		    break
	return userInput

def checkTestCase():
	print("Please enter number of test case: ")
	while True: 
		userTest = int(input())
		if userTest < 1 or userTest > 10:
		    print("Please enter test scenario between 1 and 10")
		    continue
		else:
		    break
	return userTest

def Output():	
	even = ''
	odd = ''
	for i in range(0, len(userInput)):
		if i%2 == 0:
			even += userInput[i]
			

	for i in range(0, len(userInput)):
		if i%2 != 0:
			odd += userInput[i]

	print(even + ' ' + odd)

for i in range(0, checkTestCase()):
	checkUserInput()
	Output()


	

