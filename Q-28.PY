with open("sample.txt", "r") as f:
    f.seek(5)
    print(f.read())