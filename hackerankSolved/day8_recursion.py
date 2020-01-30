entryNo = int(input("How many records would you like to add?: "))
phoneNumber = dict()


def addNumber(Name, Number):
	if Name in phoneNumber:
		print("Error")
	else:
		phoneNumber[Name] = Number

for i in range (entryNo):
    Name, Number = input("Enter the name and Number you want to add: ").split()
    Name = Name.lower()
    if len(Number) < 8:
        print("Phone Number error")
        continue
    else:
	    addNumber(Name, Number)

while True:
	print("Enter a name:(blank to quit)")
	Name = input()
	if Name == "":
		break
	if Name in phoneNumber:
		print(Name + "=" + phoneNumber[Name])
	else:
		print("Not Found")
#print(phoneNumber)