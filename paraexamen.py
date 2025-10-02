cantidad = int(input("Cantidad de numeros a validar: "))
numeros = []
for i in range(cantidad):
    num = int(input(f"Ingresa el numero {i+1}: "))
    numeros.append(num)
print(f"Numeros integrados: {', '.join(map(str, numeros))}")
print("Resultados: ")

for num in numeros:
    num_str = str(num)
    suma_digitos = sum(int(d) for d in num_str)
    suma_par = suma_digitos % 2 == 0
    num_invertido = int(num_str[::-1])
    invertido_div3 = num_invertido % 3 == 0
    es_camaleon = suma_par and invertido_div3

    if es_camaleon:
        print(f"{num} -SI (suma={suma_digitos} par, invertido={num_invertido} divisble) entre 3, -SI") 
    else:
        razones = []
        if not suma_par:
           razones.append(f"{num} -SI (suma={suma_digitos} par, invertido={num_invertido} divisible entre 3 -SI)")
        else:
            razones = []
            if not suma_par:
                razones.append(f"suma={suma_digitos} impar")
            if not invertido_div3:
                razones.append(f"invertido={num_invertido} no divisible entre 3")
            print(f"{num} -NO ({', '.join(razones)})")