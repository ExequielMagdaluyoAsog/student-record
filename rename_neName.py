
# Read the original file
with open("UEIR Simulations.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Pattern to find all neName entries
pattern = r"(neName:\s*)\S+"

# Function to replace with sequential names
def replacer(match):
    replacer.counter += 1
    return f"{match.group(1)}Node{replacer.counter:03d}"

replacer.counter = 0
new_content = re.sub(pattern, replacer, content)

# Write the updated content to a new file
with open("UEIR Simulations_renamed.txt", "w", encoding="utf-8") as file:
    file.write(new_content)

print("All neName values have been replaced with sequential names.")