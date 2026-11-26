with open("sample.txt", "w+") as f:
    f.write("Hello in w+ mode")
    f.seek(0)
    print(f.read())