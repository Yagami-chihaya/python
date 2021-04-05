poem = ["\t\n春晓",
        "春棉不觉晓",
        "处处翁啼鸟\t\n",
        "夜来风雨声",
        "\t花落知多少\t",]

poem_string = "\t\n春晓春棉不觉\t晓处处翁啼鸟\t\n夜来风雨声\t花落知多少\t"

for Isay in poem:
    print("|%s|"%Isay.ljust(5))

for Isay in poem:
    print("|%s|"%Isay.strip().ljust(5)) #strip()能删除空白字符

poem_list = poem_string.split()

print(poem_string)
print(poem_list)

join_poem = "🐶".join(poem_list)
print(join_poem)