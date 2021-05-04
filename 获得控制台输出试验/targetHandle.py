import os

getTest = os.popen(cmd="python target.py")
test = getTest.read()

print(test)
