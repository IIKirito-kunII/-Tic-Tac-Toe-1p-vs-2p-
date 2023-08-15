def printboard(xState,zState):
    def s(i): return 'X' if xState[i] else('O' if zState[i] else i+1)
    print(f"            {s(0)} | {s(1)} | {s(2)} ")
    print(f"            --|---|---")
    print(f"            {s(3)} | {s(4)} | {s(5)} ")
    print(f"            --|---|---")
    print(f"            {s(6)} | {s(7)} | {s(8)} ")

def enterValue(xState,zState):
    while True:
        value = int(input("Please enter a value: ")) - 1
        if value < 0 or value > 8: print("!Invalid value!")
        elif xState[value]==1 or zState[value]==1: print("!Position already occupied!")
        else: return value

def checkWin(xState,zState):
    win=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for line in win:
        if all(xState[i]==1 for i in line) or all(zState[i]==1 for i in line): return True
    return False
def checkDraw(xState,zState):
    if all(xState[i]==1 or zState[i]==1 for i in range(9)): return True
    return False

def restart():
        option = input("Restart[y/n]: ")
        if (option == 'y'): main()
        elif (option == 'n'): exit()
        else: print("Invalid Option!"); restart()

def main():
    xState=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    print("<<<<< Welcome to [Tic Tac Toe] >>>>>")
    while(True):
        printboard(xState,zState)
        if(turn==1):
            print("X's Chance:")
            value=enterValue(xState,zState)
            xState[value] = 1
        else:
            print("O's Chance:")
            value=enterValue(xState,zState)
            zState[value] = 1
        if checkWin(xState,zState) or checkDraw(xState,zState):
            printboard(xState,zState)
            print("==========[[GAME OVER]]===========")
            if checkWin(xState,zState):
                if(turn==1): print("-----------!!X WINS!!-------------")
                else: print("-----------!!O WINS!!-------------")
                break
            else: print("---------!!Match Draw!!-----------")
            break
        else: turn = 1-turn
    restart()

if __name__== "__main__":
    main()
