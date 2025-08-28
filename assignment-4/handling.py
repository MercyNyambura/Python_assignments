# Error Handling Lab

try:
    # Ask user for filename
    filename = input("Enter the filename you want to read: ")

    # Try to open and read
    with open(filename, "r") as file:
        data = file.read()
        print("File contents:\n")
        print(data)

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename.")

except PermissionError:
    print("Error: You don’t have permission to read this file.")

except Exception as e:
    print(f"Unexpected error: {e}")
