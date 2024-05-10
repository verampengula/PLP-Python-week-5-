# Creating the file 
try:
    with open("my_file.txt", "w") as file:
        file.write("This was very tricky to figure out. Attempts to figure it out:\n")
        file.write("5\n")
        file.write("Line 3: End of file creation.\n")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")

#  Reading and Displaying the file
try:
    with open("my_file.txt", "r") as file:
        file_contents = file.read()
        print("File Contents:\n" + file_contents)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1.\n")
        file.write("67890\n")
        file.write("Line 6: End of file appending.\n")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")
