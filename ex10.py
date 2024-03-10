def counter(words):
    count = 0
    for word in words:
        if word[0] == 'A' or word[0] == 'A':
            count += 1
    return count

words = ['Abacaxi', 'Banana', 'Amora', 'Uva', 'Maçã', 'Abóbora']
print(counter(words))