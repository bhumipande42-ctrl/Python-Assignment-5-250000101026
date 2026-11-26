digits = special = 0
with open("sample.txt", "r") as f:
    data = f.read()
    for ch in data:
        if ch.isdigit():
            digits += 1
        elif not ch.isalnum() and not ch.isspace():
            special += 1
print("Digits:", digits)
print("Special:", special)