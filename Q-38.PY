with open("sample.txt", "r") as f1:
    data = f1.read()
with open("upper.txt", "w") as f2:
    f2.write(data.upper())
print("Converted and saved.")