with open("sample.txt", "r") as f:
    data = f.read()
    words = data.split()
    print("Total words:", len(words))