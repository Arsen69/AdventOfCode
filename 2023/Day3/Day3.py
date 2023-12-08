from icecream import ic

test_data = """
12.......*..
+.........34
.......-12..
..78........
..*....60...
78..........
.......23...
....90*12...
............
2.2......12.
.*.........*
1.1.......56
"""

with open(r"2023\Day3\input.txt") as f:
    input = f.read()

def into_matrice(input_string):
    matrice = input_string.strip().split('\n')
    return matrice

def check_rectangle(matrice, line_index, index_min_nb, index_max_nb):
    symbols = set()
    for i in range(index_min_nb, index_max_nb + 1):
        if i - 1 >= 0:
            symbols.add(matrice[line_index][i-1])
            if line_index + 1 < len(matrice):
                symbols.add(matrice[line_index + 1][i-1])
            if line_index-1 >= 0:
                symbols.add(matrice[line_index - 1][i-1])
        if line_index - 1 >= 0:
            symbols.add(matrice[line_index - 1][i])
            if i + 1 < len(matrice[line_index]):
                symbols.add(matrice[line_index - 1][i + 1])
        symbols.add(matrice[line_index][i])
        if line_index + 1 < len(matrice):
            symbols.add(matrice[line_index + 1][i])
            if i + 1 < len(matrice[line_index]):
                symbols.add(matrice[line_index + 1][i + 1])
        if i + 1 < len(matrice[line_index]):
            symbols.add(matrice[line_index][i + 1])
    for symbol in symbols:
        if (not symbol.isdigit()) and symbol != '.':
            return True
    return False

def construire_nb(matrice, line_index, index_min_nb, index_max_nb):
    nombre = int(matrice[line_index][index_min_nb:index_max_nb + 1])
    return nombre

def parcourt_matrice_nombres(matrice):
    ic(matrice)
    somme = 0
    for i in range(len(matrice)):
        index_min_nb = -1
        index_max_nb = -1
        for j in range(len(matrice[i])):
            if j <= index_min_nb or j <= index_max_nb:
                continue
            char = matrice[i][j]
            if char.isdigit():
                # index min et max du nombre
                index_min_nb = j
                index_max_nb = j
                while (index_max_nb + 1) < len(matrice[i]) and matrice[i][index_max_nb + 1].isdigit():
                    index_max_nb += 1
                if check_rectangle(matrice, i, index_min_nb, index_max_nb):
                    somme += construire_nb(matrice, i, index_min_nb, index_max_nb)
    return somme


# ic(parcourt_matrice_nombres(into_matrice(test_data)))

def parcourt_matrice_symboles(matrice):
    ic(matrice)
    somme = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            char = matrice[i][j]
            if char == '*':
                somme += is_gear_2(matrice, i, j)
    return somme

def is_gear_2(matrice, line_index, column_index):
    nombres = []
    ic(line_index, column_index)
    for i in range(line_index -1, line_index + 1 + 1):
        if i < 0 or i >= len(matrice):
            continue
        indice_debut = column_index - 2
        indice_fin = column_index - 2
        for j in range(column_index - 1, column_index + 1 + 1):
            if j < 0 or j >= len(matrice[i]):
                continue
            if j <= indice_fin:
                continue
            if matrice[i][j].isdigit():
                indice_debut = j
                indice_fin = j
                while indice_debut > 0 and matrice[i][indice_debut - 1].isdigit() :
                    indice_debut -= 1
                while indice_fin + 1 < len(matrice[i]) and matrice[i][indice_fin + 1].isdigit() :
                    indice_fin += 1
                nombres.append(construire_nb(matrice, i, indice_debut, indice_fin))
    ic(nombres)
    if len(nombres) == 2:
        ic(prod(nombres))
        return prod(nombres)
    return 0

def prod(set):
    prod = 1
    for nb in set:
        prod = prod * nb
    return prod

ic(parcourt_matrice_symboles(into_matrice(input)))