# Reverse the wordlist
input_file = "500-worst-passwords.txt"  # Replace with your file name
output_file = "reversed_wordlist.txt"

# Read the file and reverse the lines
with open(input_file, "r") as f:
    lines = f.readlines()

# Write the reversed lines to a new file
with open(output_file, "w") as f:
    f.writelines(lines[::-1])

print(f"Wordlist reversed successfully! Saved as '{output_file}'.")
