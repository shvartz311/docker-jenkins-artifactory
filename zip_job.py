import sys
import os
from zipfile import ZipFile
arr = ['a', 'b', 'c', 'd']
for i in arr:
    try:
        with ZipFile(i + "_" + os.environ['VERSION'] + ".zip", 'w') as zipObj:
            file = open(i + ".txt", 'w')
            zipObj.write(i + ".txt")
    except IOError:
        print("file was not created, unable to continue, shutting down...")
        sys.exit(1)