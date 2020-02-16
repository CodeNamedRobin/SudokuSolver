import math
import time

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
    for j in range(3):
        for k in range(3):
            if (numberPossible(j + br * 3, k + 3 * bc, n, s)):
                if (len(numPossibleRow(bc, n, s)[br]) == 1 and k not in numPossibleRow(bc, n, s)[br]):
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
    return poss

def numPossibleRow(bc,n,s):
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
        z += 1
        if (z == 3):
            break
    return col
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
            break
        else:
            continue
    print("--- %s seconds to solve ---" % (time.time() - start_time))
    return s