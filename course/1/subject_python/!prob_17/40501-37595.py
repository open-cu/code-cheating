n = int(input())
arr = [int(x) for x in input().split()]

err1 = None
err2 = None

flag = True

for i in range(len(arr)):
    
    if (i+1) % 2 != arr[i] % 2:
        
        if err1 is None:
            err1 = i
            
        elif err2 is None:
            err2 = i
            
        else:
            flag = False
            break
            
if err1 is not None and err2 is None:
    print("-1 -1")
    
elif err1 is None and err2 is None and len(arr) <= 2:
    print("-1 -1")

elif err1 is None and err2 is None:
    print("1 3")
    
elif not flag or (err1 % 2 == err2 % 2):
    print("-1 -1")        

else:
    print(str(err1 + 1) + " " + str(err2 + 1))
