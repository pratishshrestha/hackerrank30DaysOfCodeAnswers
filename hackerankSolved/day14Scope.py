class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
    	for i in range(0, len(a)):
            for j in range(i+1, len(a)):
            	difference = abs(a[i]-a[j])
            	self.maximumDifference = max(self.maximumDifference, difference)



	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)