# Jogo do campo minado
# Example
# 
# For
# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]
# 
# the output should be
# minesweeper(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]]       


def minesweeper(matrix):

    campo = []
    for line in matrix:
        linha = []
        for ponto in line:
            linha.append(0)
        campo.append(linha)
    
    print(matrix)
    for i in range(0, len(campo)):
        for j in range(0, len(campo[i])):
            if j == len(matrix[i]) - 1: #lateral direita
                if i == len(matrix) - 1: #canto inferior
                    campo[i][j] += matrix[i][j-1] + matrix[i-1][j] + matrix[i-1][j-1]
                elif i == 0: #canto superior
                    campo[i][j] = matrix[i][j-1] + matrix[i+1][j] + matrix[i+1][j-1]
                else: #centro
                    campo[i][j] = matrix[i-1][j] + matrix[i+1][j] + matrix[i-1][j-1] + matrix[i][j-1] + matrix[i+1][j-1]
            elif j == 0: #lateral esquerda
                if i == len(matrix) - 1: #canto inferior
                    campo[i][j] = matrix[i][j+1] + matrix[i-1][j] + matrix[i-1][j+1]
                elif i == 0: #canto superior
                    campo[i][j] = matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
                else: #centro
                    campo[i][j] = matrix[i-1][j] + matrix[i+1][j] + matrix[i-1][j+1] + matrix[i][j+1] + matrix[i+1][j+1]
            else: #colunas do centro
                if i == len(matrix) - 1: #canto inferior
                    campo[i][j] = matrix[i][j-1] + matrix[i][j+1] + matrix[i-1][j-1] + matrix[i-1][j+1] + matrix[i-1][j]
                elif i == 0: #canto superior
                    campo[i][j] = matrix[i][j-1] + matrix[i][j+1] + matrix[i+1][j-1] + matrix[i+1][j+1] + matrix[i+1][j]
                else: #centro
                    campo[i][j] = int(matrix[i][j-1] + matrix[i][j+1] + matrix[i+1][j-1] + matrix[i+1][j+1]
                                 + matrix[i+1][j] + matrix[i-1][j-1] + matrix[i-1][j+1] + matrix[i-1][j])
                    

    return campo