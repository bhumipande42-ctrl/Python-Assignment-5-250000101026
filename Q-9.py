word = input("Enter word to search: ")
with open("sample.txt", "r") as f:
    for line in f:
        if word in line:
            print(line, end="")