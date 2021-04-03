import tools

#1.创建一个字典
person_one = {
    "name": "qiaoyang",
    "age": 18,
    "gendar": "male",
    "skill": "Super Panch"
}
print(person_one)

#tools.addCutline()
#2.给字典添加键值对
person_one["farmousWord"]="嘉然小姐我能不能做你的🐶阿"
print(person_one)

#3.删除键值对
tools.addCutline()
person_one.pop("age")
print(person_one)