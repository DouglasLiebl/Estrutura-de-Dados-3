def counter(words):
  response = []
  for i in words:
    if len(i) > 3: response.append(i)

  return response

words = ['Abacaxi', 'Banana', 'Amora', 'Uva', 'Maçã', 'Abóbora']
print(counter(words))