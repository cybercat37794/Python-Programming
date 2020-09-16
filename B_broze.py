input_sign=input('enter input')
print(input_sign)


userList = input_sign.split()
print("user list is ", userList)

for i in userList:
    if i=='.':
        print(0)
    if i=='.-':
        print(1)
    if i=='--':
        print(2)
        
    
