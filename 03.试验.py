x = 0;
while x<5:
    print("I am %d"%x);
    x+=1;

'''


阿巴阿巴阿巴阿巴


'''
'''
m = input();
print("我试试字符串能不能"+m+"相加");
'''
def ABC(char,times):
    print(char*times)

def CBA(char,times):
    row = 0
    while row<5:
        print("")
        ABC(char,times)
        row+=1
CBA("*",5)