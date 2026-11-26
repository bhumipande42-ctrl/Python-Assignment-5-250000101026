names = ["Bhumiii", "Aarav", "Diya", "Kabir", "Meera"]
with open("students.txt", "w") as f:
    for name in names:
        f.write(name + "\n")
print("Names written.")