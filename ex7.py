def get_matrix():
    matrix = []
    for i in range(0, 5):
        row = []
        for j in range(0, 5):
            e = int(input(f"Insira o elemento [{i}][{j}]: "))
            row.append(e)
        matrix.append(row)
    return matrix

def find(matrix):
  seen = []

  for i in range(5):
    for j in range(5):
      if matrix[i][j] in seen:
        print(f"Numero {matrix[i][j]} aparece novamente na posicao [{i}, {j}]")
      seen.append(matrix[i][j])       

find(get_matrix())