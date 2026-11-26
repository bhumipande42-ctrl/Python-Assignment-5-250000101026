import os
filename = "sample.txt"
print("File Name:", os.path.basename(filename))
print("Absolute Path:", os.path.abspath(filename))
print("Size:", os.path.getsize(filename), "bytes")
print("Exists:", os.path.exists(filename))
print("Is File:", os.path.isfile(filename))