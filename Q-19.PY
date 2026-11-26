n = int(input("Enter number: "))
with open("table.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{n} x {i} = {n*i}\n")
print("Table saved.")