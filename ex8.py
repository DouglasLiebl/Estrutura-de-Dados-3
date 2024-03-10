def get_matrix():
    matrix = []
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            e = int(input(f"Insira o elemento [{i}][{j}]: "))
            row.append(e)
        matrix.append(row)
    return matrix

def sum(matrix):
  response = 0
  for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
      if i == j: response += matrix[i][j]

  print(f"Soma da diagonal: {response}")

sum(get_matrix()) 