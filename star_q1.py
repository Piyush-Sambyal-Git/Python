#print a right angled triangle
for i in range(1,6):    # i is for rows
    for j in range(1,6):# j is for column
        if j<=i:
            print("*",end=" ")  #condition found using excel 
        else:
            print(" ",end="")
    print() #this prints a next line after each row so that a shape of triangle is obtained

# print its mirror image
print("")
for i in range(1,6):    # i is for rows
    for j in range(1,6):# j is for column
        if j>=6-i:
            print("*",end=" ")  #condition found using excel 
        else:
            print(" ",end="")
    print()
#more patterns
print("")
for i in range(1,6):    
    for j in range(1,6):
        if j<=6-i:
            print("*",end=" ")  
        else:
            print(" ",end="")
    print()

print("")
for i in range(1,5):    # i is for rows
    for j in range(1,8):# j is for column
        if j>=5-i and j<=3+i:
            print("*",end=" ")  #condition found using excel 
        else:
            print(" ",end=" ")
    print()

print("")
for i in range(1,5):   
    for j in range(1,8):
        if j>=i and j<=8-i:
            print("*",end=" ")  
        else:
            print(" ",end=" ")
    print()
print("")
for i in range(0,5):   
    for j in range(1,8):
        if j>=i and j<=8-i:
            print(" ",end=" ")  
        else:
            print("*",end=" ")
    print()
print("")
for i in range(1,5):    # i is for rows
    for j in range(1,8):# j is for column
        if j<=5-i or j>=3+i:
            print("*",end=" ")  #condition found using excel 
        else:
            print(" ",end=" ")
    print()
print("")
for i in range(1,6):   
    for j in range(1,6):
        if j==i or j==6-i:
            print("*",end=" ")  
        else:
            print(" ",end=" ")
    print()