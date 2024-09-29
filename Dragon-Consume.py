n = int(input())
x = int(input())
Ir = x-1  
Ans = '' 
Adventure = list(range(1,n+1)) 
i = 0
while Adventure : 
    if Ir == 0  :
        Ans += str(Adventure[i]) + ' ' 
        Adventure.pop(i)
        i-=1
        Ir = x   
    i+=1 
    Ir-=1
    if i == len(Adventure) :
        i = 0         
print(Ans)