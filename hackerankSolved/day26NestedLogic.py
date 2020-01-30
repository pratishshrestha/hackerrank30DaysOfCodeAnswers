
userInput = input().split()
returnDay = int(userInput[0])
returnMonth = int(userInput[1])
returnYear = int(userInput[2])


userInputDue = input().split()
dayDue = int(userInputDue[0])
monthDue = int(userInputDue[1])
yearDue = int(userInputDue[2])

fine = 0

if(yearDue == returnYear):
	if(returnMonth == monthDue):
		if(returnDay <= dayDue ):
			fine = 0
		else:
			noofdaysLate = returnDay - dayDue
			fine = (15*noofdaysLate)
	elif (monthDue > returnMonth):
		fine = 0

	else:
		noofMonthsLate = returnMonth - monthDue
		fine = (500 * noofMonthsLate)
elif (yearDue > returnYear):
	fine = 0
else:
	fine = 10000

print(fine)


"""if (returnDay <= dayDue and monthDue == returnMonth and yearDue == returnYear):
	fine = 0
	print(fine)

elif (returnDay > dayDue and returnMonth == monthDue and returnYear== yearDue):
	noofdaysLate = returnDay - dayDue
	print(15*noofdaysLate)

elif (returnMonth > monthDue and returnYear == yearDue):
	noofMonthsLate = returnMonth - monthDue
	print(500 * noofMonthsLate)

elif (returnYear > yearDue):
	print(10000)
"""