def invertir_array(array):
    return array[::-1]

n = int(input("Ingrese la cantidad de elementos del array: "))

array = []
for i in range(n):
    elemento = input(f"Ingrese el elemento {i+1}: ")
    array.append(elemento)
array_invertida = invertir_array(array)

print("Array original:", array)
print("Array invertida: ", array_invertida)