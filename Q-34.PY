word = input("Enter word: ")
with open("sample.txt", "r") as f:
    data = f.read()
    print("Occurrences:", data.split().count(word))