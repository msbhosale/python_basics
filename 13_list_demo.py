students = ["Amit","Ajay","Sachin","Manoj"]

print(students)

for i in range(0,len(students)):
    print(students[i])

numbers = [1,2,8,13,6]

print(numbers[4])

numbers.append(2)

print(numbers)

""" Delete by index"""
del numbers[2]

""" Deletes first matching value """
numbers.remove(2)

print(numbers)