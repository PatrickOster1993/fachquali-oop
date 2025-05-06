# Basics:
arr2 = [
	[1, 5, 23, 6, 7, 9],
	[3, 6, 0, 1, 3, 4],
	[1, 6, 78, 0, 0, 2]
] 
#= 2-dimensionales Array

arr2_elem_23 = arr2[0][2] # 23
arr1 = arr2[0]
# arr2_elem_23 = arr1[2]

# print(arr1)
# print(arr2_elem_23)

# Umgang mit Schleifen:

for array in arr2:
    # print(array)
    for element in array:
        print(element, end=' ')
    print()

print("######################")

for i in range(len(arr2)):
    arr1 = arr2[i]
    for j in range(len(arr1)):
        print(arr1[j], end=' ')
    print()

print("######################")

# Beispiel: RGB-Farbcodierung...

# von 0.. 255
# RGB = (125, 78, 33)

# rgb = [125, 78, 33] # zu kompliziert

def print_matrix(matrix):
    for row in matrix:
        # print(array)
        for col in row:
            print(col, end=' ')
        print()


# von 0.. 255
sw = 126 # lieber schwarz-weiß

sw_bild = [
    [33, 46, 12, 0, 1],
    [34, 6, 18, 9, 44],
    [1, 54, 27, 0, 0],
    [6, 39, 10, 4, 16],
    [30, 40, 12, 0, 207],
]

print_matrix(sw_bild)

print("######################")

# Einfacheres Beispiel: Schachbrett

chess = [
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],  # 1. Reihe (Schwarz)
    ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],  # 2. Reihe (Schwarz)
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],  # 3. Reihe (Leer)
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],  # 4. Reihe (Leer)
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],  # 5. Reihe (Leer)
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],  # 6. Reihe (Leer)
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],  # 7. Reihe (Weiß)
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],  # 8. Reihe (Weiß)
]

print_matrix(chess)

# Eröffnungszug:

dritter_bauer_oben_links = chess[1][2]
chess[3][2] = dritter_bauer_oben_links
chess[1][2] = 'x'

print("######################")

print_matrix(chess)
