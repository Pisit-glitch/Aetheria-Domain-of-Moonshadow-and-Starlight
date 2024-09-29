
def FIRST_WALL_U(Table,cols) :
    Tranpost = ''
    for i in Table :
        Tranpost += i[cols]
    return Tranpost.find('.')
def FIRST_WALL_D(Table,cols) :
    Tranpost = ''
    for i in Table :
        Tranpost += i[cols]
    return Tranpost.rfind('.')   
def First_WALL_L (RL) :
    for i in range(len(RL)) : 
        if RL[i] == '.' :
            return i
def First_WALL_R (RL) :
    for i in range(len(RL)-1,-1,-1) : 
        if RL[i] == '.' :
            return i
def LEFT(row,col) :
    for i in range(row) :
        WALL = First_WALL_L(Table[i])
        for j in range(col) :
            if Table[i][j] != '.' : 
                if j > 0 and j>WALL and WALL != -1: 
                    Table[i][WALL] = Table[i][j]
                    Table[i][j] = '.'
                    WALL += 1  
             
def UP(row,col) : 
    for j in range(col) :
        WALL = FIRST_WALL_U(Table,j)
        for i in range(row) :
            if Table[i][j] != '.' : 
                if i > 0 and i>WALL and WALL != -1  : 
                    Table[WALL][j] = Table[i][j]
                    Table[i][j] = '.'
                    WALL += 1
def RIGHT(row,col) :
    for i in range(row) :
        WALL = First_WALL_R(Table[i])
        for j in range(col-1,-1,-1) :
            if Table[i][j] != '.' : 
                if j < col-1 and j<WALL and WALL != -1: 
                    Table[i][WALL] = Table[i][j]
                    Table[i][j] = '.'
                    WALL -= 1   
def DOWN(row,col) :
    for j in range(col) :
        WALL = FIRST_WALL_D(Table,j)
        for i in range(row-1,-1,-1) :
            if Table[i][j] != '.' : 
                if i < row-1 and i < WALL and WALL != -1 : 
                    Table[WALL][j] = Table[i][j]
                    Table[i][j] = '.'
                    WALL -= 1 
def COUNTER_CLOCKWISE (n,row,col) :
    if n == 2 : 
        LEFT(row,col) 
    elif n == 1 : 
        UP(row,col) 
    elif n == 0 : 
        RIGHT(row,col) 
    elif n == 3 : 
        DOWN(row,col)     
    
def CLOCKWISE (n,row,col) :
    if n == 0 : 
        LEFT(row,col) 
    elif n == 1 : 
        UP(row,col) 
    elif n == 2 : 
        RIGHT(row,col) 
    elif n == 3 : 
        DOWN(row,col) 
    
row,cols = input().split()
C_CC,n = input().split()
Table = [] 
for i in range(int(row)) :
    IN = input()
    INL = [i for i in IN ]
    Table.append(INL)

n = int(n)

j = 0 
for i in range(n) :
    if C_CC == 'CLOCKWISE' :
        CLOCKWISE (j,int(row),int(cols))
    elif C_CC == 'COUNTER_CLOCKWISE' :
        COUNTER_CLOCKWISE (j,int(row),int(cols))
    j+= 1 
    if j == 4 :
        j = 0 
print('-'*(int(cols)+2))
for i in Table :
    print('|',end='')
    for j in i :
        print(j,end='')
    print('|')
print('-'*(int(cols)+2))