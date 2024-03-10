def finder(l1, l2):
  response = []
  for i in l1:
    for j in l2:
      if i == j: response.append(j)
  
  return response

print(finder(['Abacaxi', 'Banana', 'Ameixa', 'Uva', 'Maçã', 'Abóbora'], ['Abacaxi', 'Banana', 'Amora', 'Uva', 'Maçã']))