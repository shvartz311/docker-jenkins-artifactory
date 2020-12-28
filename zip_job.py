import sys
import os
from zipfile import ZipFile
arr = ['a', 'b', 'c', 'd']
for i in arr:
    try:
        file = open(i + ".txt", 'w')
    except FileNotFoundError:
        # doesn't exist, create it
        print("file was not created, failing")
        sys.exit(1)
    else:
        # exists
        print("File exists")