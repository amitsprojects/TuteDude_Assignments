# ASSIGNMENT 5:
# Module 6: Data Structures and Strings in Python

'''
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

'''

student_dict = {"Amit":95,
    "Harsh":34,
    "Naman":40
}

name = input("Enter the Student Name:")

if name in student_dict:
    print(f"{name}'s Marks: {student_dict[name]}")
else:
    print("Student not found.")


'''
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

numbers = [1,2,3,4,5,6,7,8,9,10]
first_five = numbers[0:5]
print("Extracted first five elements: " + str(first_five))
first_five.reverse()
print("Reversed list: " + str(first_five))




