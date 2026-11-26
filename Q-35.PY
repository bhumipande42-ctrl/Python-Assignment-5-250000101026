word = input("Enter word to search: ")
with open("sample.txt", "r") as f:
    data = f.read()
    if word in data:
        print("Word exists in file.")
    else:
        print("Word not found.")