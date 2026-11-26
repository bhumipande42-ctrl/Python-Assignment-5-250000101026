with open("sample.txt", "r") as f:
    f.seek(10)
    print("From position 10:", f.read())