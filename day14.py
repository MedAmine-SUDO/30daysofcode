class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        absolute_differences = [abs(i-j) for i in self.__elements for j in self.__elements]
        self.maximumDifference = max(absolute_differences)

        return self.maximumDifference

# End of Difference class