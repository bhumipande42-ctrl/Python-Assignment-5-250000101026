with open("sample.txt", "r+") as f:
    print(f.read())
    f.write("\nAdded using r+ mode.")