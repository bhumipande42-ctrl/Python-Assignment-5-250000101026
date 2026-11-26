import os
os.rename("old.txt", "new.txt")
print("File renamed.")
with open("new.txt", "r") as f:
    print(f.read())