def demo(name,gendar=True):
                #缺省参数设置了参数默认值，当函数被调用时缺少实参就会使用默认值
    if gendar == True:
        print("%s是%s"%(name,"男生"))
    elif gendar == False:
        print("%s是%s"%(name,"女生"))
    
demo("小明")

demo("小红",False)