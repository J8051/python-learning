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
