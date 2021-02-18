class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        student_average = 0
        grade = ''
        for score in self.scores:
            student_average += score
        
        student_average = student_average / len(self.scores)

        if student_average >= 90 and student_average <= 100:
            grade = 'O'
        if student_average >= 80 and student_average < 90:
            grade = 'E'
        if student_average >= 70 and student_average < 80:
            grade = 'A'
        if student_average >= 55 and student_average < 70:
            grade = 'P'
        if student_average >= 40 and student_average < 55:
            grade = 'D'
        if student_average < 40:
            grade = 'T'

        return grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())