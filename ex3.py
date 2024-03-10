notas = []
medias = []

for i in range(0, 2):
    d = [] 
    media = 0
    for j in range(0, 6):
        d.append(int(input(f"Insira a {j + 1}º nota da {i + 1}º disciplina: ")))
        media += d[j]
    medias.append((media / len(d)))
    notas.append(d)

if (medias[0] > medias[1]):
    print("A primeira disciplina teve a maior media")
else:
    print("A segunda disciplina teve a maior media")