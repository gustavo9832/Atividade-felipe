#Converta a lista minha_lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] em um conjunto para remover duplicatas e, em seguida, converta
# de volta para uma lista. Imprima a lista resultante.
minha_lista = [1,2,2,3,3,3,4,4,4,4]
meu_conjunto = set(minha_lista)
print("O conjunto será:",meu_conjunto)
listasemduplica = list(meu_conjunto)
print("A lista sem duplicados será:",listasemduplica)