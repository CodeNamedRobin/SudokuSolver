import math
import time

sudoku=[[4, -1, -1, 5, 7, 1, -1, 8, 9], [-1, 9, 5, 8, 6, 2, 4, -1, -1], [8, -1, -1, 9, 4, 3, -1, 2, 5], [1, 8, 3, 4, 9, 7, 5, 6, 2], [9, 5, 4, 2, 1, 6, 8, 7, 3], [2, -1, -1, 3, 5, 8, 1, 9, 4], [6, -1, -1, 1, 3, 5, -1, 4, 8], [-1, -1, -1, 6, 8, -1, 2, 5, -1], [5, -1, 8, 7, 2, -1, -1, -1, 6]]
def getEmptyRowCells(r,s):
    n=0
    for i in range(9):
        if(s[r][i]==-1):
            n+=1
    return n
def getEmptyColCells(c,s):
    n=0
    for i in range(9):
        if(s[i][c]==-1):
            n+=1
    return n
def getEmptyBlockCells(br,bc,s):
    n=0
    for i in range(3): # i is row here
        for j in range(3): # j is column here
            if(s[i+br*3][j+bc*3]==-1):
                n+=1
    return n
def getEmtpyCells(s):
    count = 0
    for x in range(9):
        count = count + s[x].count(-1)
    return count

def getBlock(r, c):
    block = [math.floor(r / 3), math.floor(c / 3)]
    return block


def numberPossible(r, c, n, s):
    block = getBlock(r, c)
    if (s[r][c] != -1):
        return False
    for x in range(9):
        if (s[r][x] == n):
            return False
    for x in range(9):
        if (s[x][c] == n):
            return False
    for x in range(3):
        for y in range(3):
            if (s[x + block[0] * 3][y + block[1] * 3] == n):
                return False
    return True

def checkBlockNum(br, bc, n, s):
    poss = []
    for j in range(3): # Row being checked
        for k in range(3): # Col being checked
            if (numberPossible(j + br * 3, k + 3 * bc, n, s)):
                if ((len(numPossibleCol(bc, n, s)[br]) == 1 and k not in numPossibleCol(bc, n, s)[br])):
                    if len(numPossibleRow(br,n,s)[bc])==1 and j not in numPossibleRow(br,n,s)[bc]:
                        continue
                else:
                    poss.append([j + br * 3, k + 3 * bc])
    return poss


def checkColNum(c, n, s):
    poss = []
    for i in range(9):
        if (numberPossible(i, c, n, s)):
            poss.append([i, c])
    return poss


def checkRowNum(r, n, s):
    poss = []
    for i in range(9):
        if (numberPossible(r, i, n, s)):
            poss.append([r, i])
    return poss


def possibleNums(r, c, s):
    if (s[r][c] != -1):
        return []
    poss = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # check row
    for i in range(1, 10):
        if (len(checkRowNum(r, i, s)) == 0):
            if (i in poss):
                poss.remove(i)
    # check column
    for i in range(1, 10):
        if (len(checkColNum(c, i, s)) == 0):
            if (i in poss):
                poss.remove(i)
    # check block
    block = getBlock(r, c)
    for i in range(1, 10):
        if (len(checkBlockNum(block[0], block[1], i, s)) == 0):
            if (i in poss):
                poss.remove(i)
    # check x-wing
    chickenWings=[]

    #Finds if it's a corner of an X-Wing and stores it in chickenWings
    for i in range(1,10):
        if(not checkXWing(r,c,i,s)):
            continue
        if(checkXWing(r,c,i,s)[0]==r and checkXWing(r,c,i,s)[1]==c):
            chickenWings.append(i)
    #Finds X-Wings intersecting our cell for the particular number
    if len(poss)==1:
        return poss
    for i in range(1,10):
        if i in chickenWings:
            continue
        for j in range(9):  # Check row for corners of an x-wing,j=col
            if j==c:
                continue
            if(checkXWing(r,j,i,s)!=False):
                if i in poss:
                    poss.remove(i)
        for j in range(9):  # Check column for corners of an x-wing,j=row
            if j==r:
                continue
            if(checkXWing(j,c,i,s)!=False):
                if i in poss:
                    poss.remove(i)

    return poss

def numPossibleCol(bc,n,s):
    col = []
    for i in range(3):  # Block being checked in bc
        col.append([])
        for j in range(3):  # Row in block checked
            for k in range(3):  # Column in block checked
                if (numberPossible(j + i * 3, k + bc * 3, n, s) and k not in col[i]):
                    col[i].append(k)
    c = 0
    z = 0
    while True:
        for i in range(3):
            if (len(col[i]) == 1):
                for j in range(3):
                    if j != i and col[i][0] in col[j]:
                        col[j].remove(col[i][0])
                        c += 1
        if (len(col[i]) == 2):
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        if j != i and col[i] == col[j] and k != j and k != i:
                            for l in col[i]:
                                if l in col[k]:
                                    col[k].remove(l)
                                    c += 1
        z += 1
        if (z == 3):
            break
    return col
def numPossibleRow(br,n,s):
    row = []
    for i in range(3):  # Block being checked in br
        row.append([])
        for j in range(3):  # Column in block checked
            for k in range(3):  # Row in block checked
                if (numberPossible(k+br*3,j+i*3,n,s) and k not in row[i]):
                    row[i].append(k)
    c = 0
    z = 0
    while True:
        for i in range(3):
            if (len(row[i]) == 1):
                for j in range(3):
                    if j != i and row[i][0] in row[j]:
                        row[j].remove(row[i][0])
                        c += 1
            if (len(row[i]) == 2):
                for i in range(3):
                    for j in range(3):
                        for k in range(3):
                            if j!=i and row[i]==row[j] and k!=j and k!=i:
                                for l in row[i]:
                                    if l in row[k]:
                                        row[k].remove(l)
                                        c+=1
        z += 1
        if (z == 3):
            break
    return row


#  Function Should return 2 coordinate pairs, of the top-left and bottom-right corner of the X-wing
def checkXWing(r,c,n,sudoku):
    s=sudoku
    if(s[r][c]!=-1):
        return False
    if(not numberPossible(r,c,n,s)):
        return False
    rowPos= checkRowNum(r,n,s)
    colPos= checkColNum(c,n,s)
    if(len(rowPos)!=2 and len(colPos) != 2):
        return False
    for i in rowPos: # i is thus possible columns for the X-Wing
        if(i[1]==c):
            continue
        for j in colPos: #j is thus possible rows for the X-wing, thus corner will be in the form of j[0]i[1]
            if (j[0] == r):
                continue
            if(s[j[0]][i[1]]!=-1):
                continue
            if(len(rowPos)==2 and len(colPos)==2):
                #print("Code 0")
                if (len(checkRowNum(j[0], n, s)) != 2 and len(checkColNum(i[1],n,s))!=2):
                    continue
            elif(len(rowPos)==2):
                #print("Code 1")
                if(len(checkRowNum(j[0],n,s))!=2):
                    continue
            elif(len(colPos)==2):
                #print("Code 2")
                if(len(checkColNum(i[1],n,s))!=2):
                    continue
            if(numberPossible(j[0],i[1],n,s)):
                return [r,c,j[0],i[1]]
    return False

def checkYWing(r,c,s):
    #Checks if the pivot has 2 candidates
    if(len(possibleNums(r,c,s))==2):
        return True
    #Finds the pincers

    return []
def checkPointingPair(r,c,n,s):
    #Find row pointing pairs
    if (len(checkRowNum(r, n, s)) == 2):
        if (getBlock(checkRowNum(r, n, s)[0][0], checkRowNum(r, n, s)[0][1]) == getBlock(
            checkRowNum(r, n, s)[1][0], checkRowNum(r, n, s)[1][1])):
            print("Blocks are same")
            return checkRowNum(r,n,s)

    if (len(checkRowNum(r, n, s)) == 3):
        if (getBlock(checkRowNum(r, n, s)[0][0], checkRowNum(r, n, s)[0][1]) == getBlock(
                checkRowNum(r, n, s)[1][0], checkRowNum(r, n, s)[1][1]) and getBlock(
            checkRowNum(r, n, s)[0][0], checkRowNum(r, n, s)[0][1]) == getBlock(
            checkRowNum(r, n, s)[2][0], checkRowNum(r, n, s)[2][1])):
            print("Blocks are same")
            return checkRowNum(r, n, s)
def solveSudoku(s):
    start_time= time.time()
    z = 0
    while True:
        changes = 0
        for x in range(3):
            for i in range(3):
                for k in range(1, 10):
                    if (len(checkBlockNum(x, i, k, s)) == 1):
                        s[checkBlockNum(x, i, k, s)[0][0]][checkBlockNum(x, i, k, s)[0][1]] = k
                        changes += 1
        for i in range(9):  # i is the column here
            for j in range(1, 10):  # j is the number
                if (len(checkColNum(i, j, s)) == 1):
                    s[checkColNum(i, j, s)[0][0]][i] = j
                    changes += 1
        for i in range(9):  # i is the row here
            for j in range(1, 10):  # j is the number
                if (len(checkRowNum(i, j, s)) == 1):
                    s[i][checkRowNum(i, j, s)[0][1]] = j
                    changes += 1
        for i in range(9):  # i is row
            for j in range(9):  # j is column
                if (len(possibleNums(i, j, s)) == 1):
                    s[i][j] = possibleNums(i, j, s)[0]
                    changes += 1
        if changes == 0:
            z += 1
        else:
            continue
        if z == 10:

            print(s[7][1] == -1)
            # AFTER THIS POINT DON'T USE CODE ABOVE
            break
        else:
            continue
    print("--- %s seconds to solve ---" % (time.time() - start_time))
    possNumTable=[[possibleNums(a,b,s) if(s[a][b])==-1 else [] for b in range(9)] for a in range(9)]

    for x in range(9):
        for z in range(9):
            if(s[x][z]==-1):
                s[x][z]=possNumTable[x][z]
    for i in range(9):
        print(s[i])
    return s
'''wings=[[checkYWing(i,j,sudoku) if sudoku[i][j]==-1 else [] for j in range(9)] for i in range(9)]
for i in range(9):
    print(wings[i])'''

