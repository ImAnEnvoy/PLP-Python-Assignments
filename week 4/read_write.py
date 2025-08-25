# Python program to read a file, modify its content, and write to a new file

input_file = "myText.txt"     # Existing file
output_file = "output.txt"   # New file

try:
    # Step 1: Open and read the input file
    with open(input_file, "r") as f:
        content = f.read()

    # Step 2: Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Step 3: Write the modified content to the output file
    with open(output_file, "w") as f:
        f.write(modified_content)

    print(f"Modified content written to '{output_file}' successfully!")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
