upper = lower = 0
with open("sample.txt", "r") as f:
    data = f.read()
    for ch in data:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)