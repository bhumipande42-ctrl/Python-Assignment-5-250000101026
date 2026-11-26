text = input("Enter text: ")
with open("user.txt", "w") as f:
    f.write(text)
print("Saved.")