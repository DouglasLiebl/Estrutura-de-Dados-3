def get_matrix():
    matrix = []
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            e = int(input(f"Insira a {j + 1}º do aluno {i + 1}: "))
            row.append(e)
        matrix.append(row)
    return matrix

def average(notes):
  averages = []
  for i in notes:
    sum = 0
    for j in i:
      sum += j
    sum = sum / len(i)
    averages.append(sum)

  return averages

def greater(averages):
  greater = 0
  student = 0

  for i in range(0, 3):
    if (averages[i] > greater):
      greater = averages[i]
      student = i + 1

  print(f"O aluno com a maior media foi o {student}")

greater(average(get_matrix()))