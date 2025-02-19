#You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
# 1) Each row must contain the digits 1-9 without duplicates.
# 2) Each column must contain the digits 1-9 without duplicates.
# 3) Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false
# Note: A board does not need to be full or be solvable to be valid.
def main():
    # problem input, can be changed!
    board = [["1","2",".",".","3",".",".",".","."],
             ["4","1",".","5",".",".",".",".","."],
             [".","9","8",".",".",".",".",".","3"],
             ["5",".",".",".","6",".",".",".","4"],
             [".",".",".","8",".","3",".",".","5"],
             ["7",".",".",".","2",".",".",".","6"],
             [".",".",".",".",".",".","2",".","."],
             [".",".",".","4","1","9",".",".","8"],
             [".",".",".",".","8",".",".","7","9"]]

    # create x and y coordinates for our board
    x=1
    y=1
    # created list of lists for our rows and columns and set valid to True until proven otherwise
    row = [[],[],[],[],[],[],[],[],[]]
    column = [[],[],[],[],[],[],[],[],[]]
    valid = True
    # while loop that iterates down the board
    while y <= 9:
        if board[y-1][x-1] != ".":
            # if there is a number we want to add that number to our row and column list
            row[y-1].append(board[y-1][x-1])
            column[x-1].append(board[y-1][x-1])  
            
        # once we reach the end of the board in the x direction we can move our y 
        # value down the board and reset our x
        if x % 9 == 0:
            x = 0
            y+=1
        x+=1
    
    # set our x and y coordinates like before
    x=0
    y=0
    # create a list of lists for each square on our board
    square = [[],[],[],[],[],[],[],[],[]]
    squareNum = 0
    # while loop to iterate through each square
    while squareNum < 9:
        for i in range(3):
            # check each square in a 3x3 perimeter and add them to our list of squares
            if board[y+i][x]!=".":
                square[squareNum].append(board[y+i][x])
            if board[y+i][x+1]!=".":   
                square[squareNum].append(board[y+i][x+1])
            if board[y+i][x+2]!=".":
                square[squareNum].append(board[y+i][x+2])
        
        squareNum += 1
        x+=3
        # when our x direction gets to the end we move downward and reset x
        if x >= 9:
            y += 3
            x = 0
    
    # for loop that iterates through each list of lists 
    for i in range(9):
        # for each list in our lists, we can compare the length of that list to the set of that list,
        # since sets get rid of duplicates, if they are not equal we can conclude the board is not valid
        if len(set(row[i])) != len(row[i]):
            valid = False
            break
        if len(set(column[i])) != len(column[i]):
            valid = False
            break
        if len(set(square[i])) != len(square[i]):
            valid = False
            break
    # print our answer
    print(valid)
main()