peso = float(input("informe peso"))
altura = float(input("informe altura"))

imc =peso/(altura*altura)

if imc < 18.5:
    print("abaixo do peso)")

elif imc >= 18.5 and imc <= 24.9:
    print("abaixo do peso")

elif imc >= 25.0 and imc <= 29.9:
    print("pré obesidade")

elif imc >= 30.0 and imc <= 34.9:
    print("obesidade grau 1")

elif imc >= 35.0 and imc <= 39.9:
    print("obesidade grau 2")

else:
    print("obesidade grau 3")

