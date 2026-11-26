import os
filename = "sample.txt"
print("Exists:", os.path.exists(filename))
if os.path.exists(filename):
    print("Size:", os.path.getsize(filename), "bytes")