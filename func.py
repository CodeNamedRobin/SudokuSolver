import math

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

def solveSudoku(s):
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
    return s