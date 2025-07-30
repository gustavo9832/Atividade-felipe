# Dados os conjuntos conjunto_a = {1, 2, 3, 4} e conjunto_b = {3, 4, 5, 6},
# realize as seguintes operações e imprima os resultados:
#União de conjunto_a e conjunto_b.
#Interseção entre conjunto_a e conjunto_b.
#Diferença entre conjunto_a e conjunto_b.
conjunto_a = {1,2,3,4}
conjunto_b = {3,4,5,6}
conjTotal = conjunto_a.union(conjunto_b)
print(conjTotal)
intersect= conjunto_a.intersection(conjunto_b)
print(intersect)
diferconj = conjunto_a.difference(conjunto_b)
print(diferconj)