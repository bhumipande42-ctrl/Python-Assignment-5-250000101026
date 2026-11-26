name = input("Enter name: ")
roll = input("Enter roll no: ")
marks = input("Enter marks: ")
with open("student.txt", "w") as f:
    f.write(f"Name: {name}\nRoll: {roll}\nMarks: {marks}\n")
print("Saved.")