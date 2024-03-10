numbers = []
non_negative = []
for i in range(0, 5):
    numbers.append(int(input(f"Insira o {i + 1}º numero: ")))
    if (numbers[i] < 0):
        non_negative.append(0)
        continue
    non_negative.append(numbers[i])

print(f"Original: {numbers} \nNew: {non_negative}")