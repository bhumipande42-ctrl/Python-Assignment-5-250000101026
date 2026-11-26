import os
dirname = input("Enter directory name: ")
if not os.path.exists(dirname):
    os.mkdir(dirname)
    print("Directory created.")
else:
    print("Directory already exists.")