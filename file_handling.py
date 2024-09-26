# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("Hello, World!\n")
        file.write("The number is 42\n")
        file.write("Python file handling is easy!\n")
    print("File created and initial content written.")

    # File Reading and Display
    with open("my_file.txt", 'r') as file:
        content = file.read()
    print("\n--- File Content After Creation ---")
    print(content)

    # File Appending
    with open("my_file.txt", 'a') as file:
        file.write("Appending new line 1.\n")
        file.write("Appending new line 2.\n")
        file.write("Appending new line 3.\n")
    print("Additional content appended.")

    # Displaying the updated content
    with open("my_file.txt", 'r') as file:
        updated_content = file.read()
    print("\n--- File Content After Appending ---")
    print(updated_content)

except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
except PermissionError as p_error:
    print(f"Error: {p_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operations completed.")
