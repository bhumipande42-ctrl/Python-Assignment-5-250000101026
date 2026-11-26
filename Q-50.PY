import os
# Create and write
f = open("temp.txt", "w")
f.write("Hello, this is a test file.")
f.close()

# Read
f = open("temp.txt", "r")
print("Contents:", f.read())
f.close()
print("Is closed?", f.closed)

# Delete
os.remove("temp.txt")
print("File deleted.")
print("Exists after delete?", os.path.exists("temp.txt"))