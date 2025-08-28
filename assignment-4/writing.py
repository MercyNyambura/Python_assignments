# File Read 

try:
    # Read input.txt
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Modify the content to uppercase
    modified_content = content.upper()

    # Write to output.txt
    with open("output.txt", "w") as outfile:
        outfile.write("=== MODIFIED CONTENT ===\n")
        outfile.write(modified_content)

    print("Success! Modified file 'output.txt' has been created.")

except Exception as e:
    print(f"⚠️ An error occurred: {e}")
