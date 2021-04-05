allPerson = []

def showMain():
    print("*"*50)
    print("")
    print("欢迎使用名片管理系统!!")
    print("")
    print("请选择你要执行的操作")
    print("")
    print("【1】添加名片")
    print("【2】查询所有名片")
    print("【3】查询个人名片")
    print("")
    print("【0】退出系统")
    print("")
    print("*"*50)

def createPerson():
    name = input("请输入你的名字") 
    number = input("请输入你的手机号")    
    sex = input("请输入你的性别")    
    email = input("请输入你的邮箱")    
    onePerson = {
        "name": name,
        "number": number,
        "sex": sex,
        "email": email
    }   
    allPerson.append(onePerson)

def showAllPerson():
    print("名字\t\t号码\t\t性别\t\t邮箱")
    for m in allPerson:
        print("%s\t\t%s\t\t%s\t\t%s"%(m["name"],m["number"],m["sex"],m["email"]))


def infoPerson():
    infoName = input("请输入你要查找的名字")
    for m in allPerson:
        if m["name"] == infoName:
            print("查询成功！！")
            print(m)
            break
    else:
        print("查询失败，系统无此人！")
