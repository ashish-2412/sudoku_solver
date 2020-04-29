board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def printboard(s):
    for i in range(len(s)):
        if i%3==0:
            print("-----------------------")
        for j in range(len(s[0])):
            if j%3==0:
                print("|",end=" ")
            print(s[i][j],end=" ")
        print()
            
def findempty(s):
    for i in range(len(s)):
         for j in range(len(s[0])):
             if(s[i][j]==0):
                 return (i,j)
    return None
def isvalid(s,num,pos):
    #row check
    for i in range(len(s[0])):
        if s[pos[0]][i]==num and i!=pos[1]:
            return False
    #col check
    for i in range(len(s)):
        if s[i][pos[1]]==num and i!=pos[0]:
            return False
    #box check
    #determine box
    box_i=pos[0]//3
    box_j=pos[1]//3

    for i in range(box_i*3,box_i*3+3):
        for j in range(box_j*3,box_j*3+3):
            if s[i][j]==num and i!=pos[0] and j!=pos[1]:
                return False
    return True
    
    
def solve(s):
    find=findempty(board)
    if not find:
        return True
    else:
        row,col=find
    for i in range(1,10):
        if isvalid(s,i,find):
            s[row][col]=i

            if solve(s):
                return True
            
            s[row][col]=0
    return False
