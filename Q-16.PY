# Write mode - overwrites old data
with open("demo.txt", "w") as f:
    f.write("Hello\n")

# Append mode - adds to existing data without deleting
with open("demo.txt", "a") as f:
    f.write("World\n")

with open("demo.txt", "r") as f:
    print(f.read())