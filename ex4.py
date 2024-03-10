numbers = []
for i in range(0, 4):
    numbers.append(int(input(f"Insira o {i + 1}º numero: ")))


def change_order(numbers):
  for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] > numbers[j]: 
        numbers[i], numbers[j] = numbers[j], numbers[i]
  
  return numbers

print(f"Ordem crescente: {change_order(numbers)}")