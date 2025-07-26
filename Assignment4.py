'''
Module 5: Files, Exceptions, and Errors in Python

Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''


try:
    file = open('sample.txt', 'r')
    n = 1
    for line in file:
        print(f"Line {n}: {line.strip()}")
        n += 1
    file.close()
except FileNotFoundError:
    print("Error: sample.txt not found.")



'''
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

'''

# Step 1: Write user input to a file
line1 = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(line1 + "\n")

print("Data successfully written to output.txt.\n")

# Step 2: Append additional data to the same file
line2 = input("Enter additional text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(line2 + "\n")

print("Additional data appended successfully to output.txt.\n")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
try:
    with open("output.txt", "r") as file:
        line_number = 1
        for line in file:
            print(f"Line{line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print("Error: output.txt not found.")
