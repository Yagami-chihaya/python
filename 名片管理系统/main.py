import card_tools

card_tools.showMain()

while True:

    print("-"*50)
    
    userCommand = input("请输入你要执行的操作")
    print("你选择了【%s】！"%userCommand)

    #新增名片
    if userCommand == "1":
        card_tools.createPerson()
    #显示全部名片
    elif userCommand == "2":
        card_tools.showAllPerson()
    #查询名片
    elif userCommand == "3":
        card_tools.infoPerson()
    elif userCommand == "0":
        print("运行结束，欢迎下一次使用")
        break
    else:
        print("输入了无效命令，请重新输入")