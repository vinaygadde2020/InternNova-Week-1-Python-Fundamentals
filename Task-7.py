# 1. String operations
text = "Python Data Analytics"
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Replace:", text.replace("Python", "Advanced Python"))
print("Find:", text.find("Data"))
# 2. List operations
numbers = [30, 10, 20]
numbers.append(40)
print("After append:", numbers)
numbers.remove(10)
print("After remove:", numbers)
numbers.sort()
print("After sort:", numbers)
# 3. Tuple creation and indexing
student = ("Vinay", "Data Science", 20)
print("Tuple:", student)
print("First element:", student[0])
# 4. Dictionary storing student information
student_info = {
    "Name": "Vinay",
    "College": "Aditya University",
    "Branch": "Data Science"
}
print("Student Information:", student_info)
# 5. Set operations
subjects = {"Python", "SQL", "Excel"}
subjects.add("Power BI")
print("After add:", subjects)
subjects.remove("Excel")
print("After remove:", subjects)