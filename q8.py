for i in range(1,6,1):
    for j in range(1,6,1):
        if j>=6-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("")
for i in range(1,6,1):
    for j in range(1,6,1):
        if j>=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("")
for i in range(1,5,1):
    for j in range(1,8,1):
        if j>=5-i and j<=3+i :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



