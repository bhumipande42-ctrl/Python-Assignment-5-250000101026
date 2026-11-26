f = open("sample.txt", "r")
print(f.read())
f.close()
print("Is closed?", f.closed)