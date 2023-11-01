# Part 1: Calculate Grade Average

username = input("Enter your name: ")
mathScore = int(input("Enter your Math score: "))
englishScore = int(input("Enter your English score: "))
scienceScore = int(input("Enter your Science score: "))
averageGrade = (mathScore + englishScore + scienceScore) / 3
averageGrade = format(float(averageGrade), '.2F')
print("Hello, " + username + "! Your average grade is: " + averageGrade)

# Part 2: Simple Interest Calculator 

principalAmount = float(input("Enter the principle amount: "))
annualInterestRatePercent = float(input("Enter the annual interest rate (in percentage): "))
annualInterestRateDecimal = annualInterestRatePercent / 100
numbOfyears = float(input("Enter the number of years: "))
simpleInterest = principalAmount * annualInterestRateDecimal * numbOfyears
simpleInterest = format(simpleInterest, '.2F')

print("Principal Amount: $" + str(int(principalAmount)))
print("Annual Interest Rate: " + str(int(annualInterestRatePercent)) + "%")
print("Number of Years: " + str(int(numbOfyears)))
print("Simple Interest Earned: $" + simpleInterest)

#1.The average grade of the students

numOfStudents = input("Enter the number of students: ")

listOfGrades = []
i = 0
while len(listOfGrades) < int(numOfStudents):
  i += 1
  grade = input("Enter the grade for student " + str(i) + ": ")
  listOfGrades.append(grade)

total = 0
for x in listOfGrades:
  total += int(x)

average = total / len(listOfGrades)
print("Average Grade: " + str(average))

#2. The highest grade of the students

highest = listOfGrades[0]
for j in listOfGrades:
  if j > highest:
    highest = j
print("Highest Grade: "+ str(highest))


#2. The lowest grade of the students

lowest = listOfGrades[0]
for y in listOfGrades:
  if y < lowest:
    lowest = y
print("Lowest Grade: " + str(lowest))


#3. The number of students who passed

studentsPassed = 0
for i in listOfGrades:
  if int(i) >= 60:
    studentsPassed += 1
print("Number Of Students Passed: " + str(studentsPassed))


#4. The number of students who failed

studentsFailed = 0
for a in listOfGrades:
  if int(a) < 60:
    studentsFailed += 1
print("Number of Students failed: " + str(studentsFailed))


#5. Grade Modification

modifiedGrades = []

for originalGr in listOfGrades:
  originalGr = int(originalGr)
  if originalGr < average:
    originalGr += 5
  modifiedGrades.append(originalGr)
print("Modified Grades: " + str(modifiedGrades))

#6. Letter Grades

letterGrades = []
for modGr in modifiedGrades:
  modGr = int(modGr)
  if modGr < 60:
    letterGrades.append("F")
  if modGr >= 90:
    letterGrades.append("A")
  if modGr >= 60 and modGr <= 69:
    letterGrades.append("D")
  if modGr >= 70 and modGr <= 79:
    letterGrades.append("C")
  if modGr >= 80 and modGr <= 89:
    letterGrades.append("B")
print("Letter Grades: " + str(letterGrades))
