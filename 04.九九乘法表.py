n = 1
while n<=9:
    m = 1
    while m<=n:
        if(m*n>=10):
            print("%d*%d=%d"%(m,n,m*n),end=" ")
        else:
            print("%d*%d=%d"%(m,n,m*n),end="  ")
        m+=1
    print("")
    n+=1
