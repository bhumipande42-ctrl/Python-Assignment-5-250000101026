with open("sample.txt", "r") as f:
    print("Position:", f.tell())
    f.read(5)
    print("After reading 5 chars:", f.tell())