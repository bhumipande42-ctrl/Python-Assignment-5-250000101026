with open("sample.txt", "r") as f1:
    data = f1.read()
with open("reverse.txt", "w") as f2:
    f2.write(data[::-1])
print("Reversed and saved.")