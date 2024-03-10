def get_matrix():
    matrix = []
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            e = int(input(f"Insira o elemento [{i}][{j}]: "))
            row.append(e)
        matrix.append(row)
    return matrix

def verify_matrix(matrix):
  for i in matrix:
    for j in i:
      if (j % 2 != 0): return False
  
  return True

matrix = get_matrix()
print(matrix)
if verify_matrix(matrix): print("Matrix positiva")
else: print("Matrix com numeros negativos")