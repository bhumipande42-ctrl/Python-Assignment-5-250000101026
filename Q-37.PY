ch = input("Enter character: ")
with open("sample.txt", "r") as f:
    for line in f:
        if line.startswith(ch):
            print(line, end="")