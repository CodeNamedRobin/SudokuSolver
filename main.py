from tkinter import *
from func import *
window = Tk()
sudoku2=[]
window.title("Sudoku Solver")
size=966
window.geometry(str(size) + "x" + str(size))
entries=[]
main = Frame(window)
main.pack()
def solve(s):
    outputSudoku(solveSudoku(s))
def outputSudoku(s):

    for i in range(9):
        for j in range(9):
            if s[i][j]==-1:
                Label(main, text=" ", font=("Arial", 35), image=PhotoImage(), height=100, width=100, bd=1,
                      compound='center', relief='solid').grid(column=j, row=i)
            else:
                Label(main, text=str(s[i][j]), font=("Arial", 35), image=PhotoImage(), height=100, width=100, bd=1,
                      compound='center', relief='solid').grid(column=j, row=i)
    Button(main, text="solve", command= lambda: solve(s)).grid(column=0, row=9)
def clearScreen():
    global main, window
    main.destroy()
    main=Frame(window)
    main.pack()
def getInput():
    sudoku2 = [[int(entries[x + i * 9].get()) if (entries[x + i * 9].get()) != '' else -1 for x in range(9)] for i in range(9)]
    clearScreen()
    outputSudoku(sudoku2)
def emptyScreenInput():
    for i in range(9):
        for j in range(9):
            e=Entry(main, width=1, font=("Arial", 35), bd=1, relief='solid', justify='center')
            e.grid(column=j, row=i, ipady=24, ipadx=36)
            entries.append(e)
    Button(main, text="test", command=getInput).grid(column=0, row=9)



emptyScreenInput()


window.mainloop()