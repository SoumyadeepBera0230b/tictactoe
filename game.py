
def print_board(x, o):
    zero = x[0] if x[0]=='X' else (o[0] if o[0]=="O" else 0)
    one = x[1] if x[1]=='X' else (o[1] if o[1]=="O" else 1)
    two = x[2] if x[2]=='X' else (o[2] if o[2]=="O" else 2)
    three = x[3] if x[3]=='X' else (o[3] if o[3]=="O" else 3)
    four = x[4] if x[4]=='X' else (o[4] if o[4]=="O" else 4)
    five = x[5] if x[5]=='X' else (o[5] if o[5]=="O" else 5)
    six = x[6] if x[6]=='X' else (o[6] if o[6]=="O" else 6)
    seven = x[7] if x[7]=='X' else (o[7] if o[7]=="O" else 7)
    eight = x[8] if x[8]=='X' else (o[8] if o[8]=="O" else 8)
    
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
    
def winner(x, o):
    win = [[0, 1, 2], [3, 4, 5], [6, 7,8 ], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for i in win:
        if x[i[0]] == "X" and x[i[1]] == "X" and x[i[2]] == "X":
            print_board(x, o)
            print("X is the Winner of the match")
            return 1
        elif o[i[0]] == "O" and o[i[1]] == "O" and o[i[2]] == "O":
            print_board(x, o)
            print("O is the winner of the match")
            return 0
    
    return -1
    
if __name__ == "__main__":
    xValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    oValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    li = []
    print("Welcome to the Game...")
    
    while True:
        print_board(xValues, oValues)
        if turn == 1:
            print("X's turn now")
            while True:
                value = int(input("Enter the value: "))
                if value >= 0 and value <= 8 and value not in li:
                    xValues[value] = "X"
                    li.append(value)
                    break
        
        else:
            print("O's turn now")
            while True:
                value = int(input("Enter the value: "))
                if value >= 0 and value <= 8 and value not in li:
                    oValues[value] = "O"
                    li.append(value)
                    break
        
        res = winner(xValues, oValues)
        if res != -1:
            break
        turn = 1 - turn
    print("Match Ended")
    