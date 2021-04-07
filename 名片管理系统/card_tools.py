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
    print("%-18s%-16s%-18s%s"%("姓名","电话号码","性别","邮箱"))
    
    
    for m in allPerson:
        print("%-20s%-20s%-20s%-20s"%(m["name"],m["number"],m["sex"],m["email"]))


def infoPerson():
    infoName = input("请输入你要查找的名字")
    for m in allPerson:
        if m["name"] == infoName:
            print("查询成功！！")
            print("姓名:%-5s电话号码:%-5s性别:%-5s邮箱:%-5s"%(m["name"],m["number"],m["sex"],m["email"]))
            ###########################################
            while True:
                print("请选择对该名片的操作")
                print("")
                print("【1】删除名片\t【2】修改名片\t【0】返回上一级菜单")
                userChoose = input("")
                if userChoose == "1":
                    delPerson(m)
                elif userChoose == "2":
                    changePerson(m)
                elif userChoose == "0":
                    print("返回成功")
                    break
                else:
                    print("无效命令")



def delPerson(someone):
    allPerson.remove(someone)
    print("删除已执行")

def changePerson(someone):
    someone["name"] = input("输入修改后的姓名")
    someone["number"] = input("输入修改后的电话号码")
    someone["sex"] = input("输入修改后的性别")
    someone["email"] = input("输入修改后的邮箱")

