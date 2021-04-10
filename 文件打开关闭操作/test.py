file = open("文件打开关闭操作/README.txt",encoding="UTF-8")

readFile = file.read()

print(readFile)

file.close()
