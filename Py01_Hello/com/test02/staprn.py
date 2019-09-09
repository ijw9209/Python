# 1
for i in range(5): #0 1
    for j in range(i+1): #1 2
        print('*',end='')
    print()
    
    
print("==================")
# 2 
for i in range(5): # 0
    for j in range(5-i): 
        print('*',end='') 
    print()    
# 3    
print("==================")
for i in range(5): #5
    for j in range(5-i):  #0 1 2 3 
            print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()    
# 4        
print("==================")
for i in range(5):
    for j in range(i+1):
        print(' ',end='')
    for j in range(5-i):
        print('*' , end='')
    print()    
# 5
print("==================")
for i in range(5):
    for j in range(5-i):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print()        