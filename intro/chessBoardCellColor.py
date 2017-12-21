# Given two cells on the standard chess board, 
# determine whether they have the same color or not.
# 
# Example
# 
# For cell1 = "A1" and cell2 = "C3", the output should be
# chessBoardCellColor(cell1, cell2) = true.


def colorcell(cell):
    if cell[0].lower() in 'aceg':
        return True if (int(cell[1])%2==0) else False
    else:
        return False if (int(cell[1])%2==0) else True


def chessBoardCellColor(cell1, cell2):
    return colorcell(cell1) == colorcell(cell2)