class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        

    def calculate(self):
        averageScore = sum(self.scores)//len(self.scores)
        if (90 <= averageScore) and (averageScore <= 100):
            return "O"
        elif (80 <= averageScore) and (averageScore < 90):
            return "E"
        elif (70 <= averageScore) and (averageScore < 80):
            return "A"
        elif ( 55 <= averageScore) and (averageScore <70):
            return "P"
        elif (40 <= averageScore) and (averageScore < 55):
            return "D"
        elif (averageScore < 40):
            return "T"
        else:
            return ""

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2] 
numScores = int(input())
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())