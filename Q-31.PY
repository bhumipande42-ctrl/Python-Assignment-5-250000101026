count = 0
with open("sample.txt", "r") as f:
    data = f.read()
    for ch in data:
        if ch.lower() in "aeiou":
            count += 1
print("Vowels:", count)