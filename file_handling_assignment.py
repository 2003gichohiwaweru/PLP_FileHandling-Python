def write_to_file():
    try:
        # Open file in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Writing three lines of text to the file
            file.write("Hello, this is line 1.\n")
            file.write("12345\n")
            file.write("Another line with 3.14\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred: {e}")
    finally:
        print("Write operation completed.")

def read_and_display_file():
    try:
        # Open file in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display each line
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())  # Strip to remove extra newline characters
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to read the file.")

def append_to_file():
    try:
        # Open file in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Appending three more lines of text
            file.write("Appending line 1.\n")
            file.write("67890\n")
            file.write("Appending more text.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred: {e}")
    finally:
        print("Append operation completed.")

# Writing to the file
write_to_file()

# Reading and displaying the file contents
read_and_display_file()

# Appending more content to the file
append_to_file()

# Reading and displaying the file contents again
read_and_display_file()
