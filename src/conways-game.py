import copy
print('Patterns in Conway\'s Game of Life')

actualMatrix = [[0,0,0,0,0,0], 
                [0,0,1,0,0,0],
                [0,0,0,1,0,0],
                [0,1,1,1,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0]]

nextMatrix = [[0,0,0,0,0,0], 
                [0,0,1,0,0,0],
                [0,0,0,1,0,0],
                [0,1,1,1,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0]]



def printMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def getNextMatrix(actual, next):
    for m in range(len(actual)):
        for n in range(len(actual[m])):
            nextElement = getValuePerElement(m,n,actual)
            next[m][n] = nextElement

def getValuePerElement(row, column, matrix):
    # print('row', row, 'column', column, 'element', matrix[row][column])
    lengthMatrix = len(matrix)
    lengthRow = len(matrix[row])
    if row == 0:
        startRow = 0
        finalRow = row + 2
    elif row == lengthMatrix-1:
        startRow = lengthMatrix-2
        finalRow = lengthMatrix
    else:
        startRow = row - 1
        finalRow = row + 2

    if column == 0:
        startColumn = 0
        finalColumn = column + 2
    elif column == lengthMatrix-1:
        startColumn = lengthRow-2
        finalColumn = lengthRow
    else:
        startColumn = column - 1
        finalColumn = column + 2

    neighborsSum = 0
    newValue = 0

    for i in range(startRow, finalRow):
        for j in range(startColumn, finalColumn):
            if i == row and j == column:
                neighborsSum = neighborsSum
            else:
                neighborsSum += matrix[i][j]
  
    
    

    if matrix[row][column] == 0 and neighborsSum == 3:
        newValue = 1
    elif matrix[row][column] == 1 and (neighborsSum == 3 or neighborsSum == 2):
        newValue = 1
   

    # print('row, column, sum newValue, oldvalue', row, column, neighborsSum, newValue, matrix[row][column])
    # print()
    return newValue
    

print(len(actualMatrix), ' actual matix len')
print(len(actualMatrix[0]), ' actual matix len 0')
printMatrix(actualMatrix)   

print('Calculate next matrix 1')
getNextMatrix(actualMatrix, nextMatrix)
actualMatrix = copy.deepcopy(nextMatrix)
printMatrix(nextMatrix)
print()
print('Calculate next matrix 2')

getNextMatrix(actualMatrix, nextMatrix)
actualMatrix = copy.deepcopy(nextMatrix)
printMatrix(nextMatrix)

getNextMatrix(actualMatrix, nextMatrix)
printMatrix(nextMatrix)