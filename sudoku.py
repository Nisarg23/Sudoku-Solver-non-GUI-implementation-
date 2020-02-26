# sudoku
not_solved = [5, 3, None, None, 7, None, None, None, None,
              6, None, None, 1, 9, 5, None, None, None,
              None, 9, 8, None, None, None, None, 6, None,
              8, None, None, None, 6, None, None, None, 3,
              4, None, None, 8, None, 3, None, None, 1,
              7, None, None, None, 2, None, None, None, 6,
              None, 6, None, None, None, None, 2, 8, None,
              None, None, None, 4, 1, 9, None, None, 5,
              None, None, None, None, 8, None, None, 7, 9]

# prints sudoku template puzzle
for i in range(9):
    for j in range(9):
        if not_solved[i*9+j] is None:
            print("|_  _|", end="")
        else:
            print("|_"+ str(not_solved[i*9+j])+"_|", end="")
    print("")


# solution to sudoku
solved = [5, 3, 4, 6, 7, 8, 9, 1, 2,
          6, 7, 2, 1, 9, 5, 3, 4, 8,
          1, 9, 8, 3, 4, 2, 5, 6, 7,
          8, 5, 9, 7, 6, 1, 4, 2, 3,
          4, 2, 6, 8, 5, 3, 7, 9, 1,
          7, 1, 3, 9, 2, 4, 8, 5, 6,
          9, 6, 1, 5, 3, 7, 2, 8, 4,
          2, 8, 7, 4, 1, 9, 6, 3, 5,
          3, 4, 5, 2, 8, 6, 1, 7, 9]
