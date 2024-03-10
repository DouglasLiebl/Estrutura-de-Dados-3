numbers = []
sum = 0
negatives = 0
for i in range(0, 5):
    numbers.append(int(input(f"Insira o {i + 1}º numero: ")))
    if (numbers[i] >= 0):
        sum += numbers[i]
        continue
    negatives += 1

print(f"Soma positivos: {sum} \nNumero de negativos: {negatives}")