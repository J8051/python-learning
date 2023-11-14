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

# Read csv file & Analyze data
import csv

list_sales_data = []


def read_sales_data(file_path):
  with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      for k, v in row.items():
        if not v:
          if k == "Price" or k == "Quantity":
            row[k] = 0
          elif k == "Category" or k == "Product":
            row[k] = "N/A"
      list_sales_data.append(row)


read_sales_data("sales_data.csv")
print("The first five rows of Sales data are: \n" + str(list_sales_data[0:5]) +
      "\n")


def calculate_total_sales(list):
  total_sales = 0
  price_times_quantity = 0
  for x in list:
    for y in x:
      price_times_quantity = int(x["Price"]) * int(x["Quantity"])
    total_sales += price_times_quantity

  print("The Total Sales of all the Products is: $" + str(total_sales) + "\n")


calculate_total_sales(list_sales_data)

analysis_data = {}


def category_analysis_helper(list, category):
  average_price = int(0)
  category_length = []
  price_times_quantity = 0
  total_sales = 0
  for x in list:
    for y in x:
      if y == "Price" and x["Category"] == category:
        category_length.append(y)
        average_price += int(x["Price"])
        price_times_quantity = int(x["Price"]) * int(x["Quantity"])
        total_sales += price_times_quantity
        analysis_data[category] = [average_price, total_sales]

  average_price = average_price / len(category_length)
  average_price = format(average_price, ".2f")
  total_sales = format(total_sales, ".2f")
  print("Average Price of " + category + " is: $" + str(average_price))
  print("Total Sales of " + category + " is: $" + str(total_sales) + "\n")


category_list = [
    "Electronics", "Accessories", "Appliances", "Footwear", "Apparel", "Art",
    "Furniture", "Books"
]


def category_analysis(list):
  for x in list:
    category_analysis_helper(list_sales_data, x)


category_analysis(category_list)


def bestselling_product(list):
  best_seller = 0
  product_name = ""
  for x in list:
    if int(x["Quantity"]) > int(best_seller):
      best_seller = x["Quantity"]
      product_name = str(x["Product"])

  print("The Best Selling Product is " + str(product_name) + "\n")


bestselling_product(list_sales_data)


def sales_recommendations(data):
  least_units_sold = float("inf")
  category_name = ""
  for category in category_list:
    (data[category])
    units_sold = data[category][1] / data[category][0]
    if units_sold < least_units_sold:
      least_units_sold = units_sold
      category_name = category

  print(f"The category with the lowest sales is the {category_name} category"
        f" this category only sold {least_units_sold} unit(s), consider"
        " lowering the price")


sales_recommendations(analysis_data)