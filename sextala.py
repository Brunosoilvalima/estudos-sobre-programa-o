def soma(numero1, numero2):
    print(numero1 + numero2)


def subtraçao(numero1, numero2):
    print(numero1 - numero2)


def multiplicacao(numero1, numero2):
    print(
        numero1 * numero2)


def divisao(numero1, numero2):
    print(numero1 / numero2)




opcao = int(input("qual operacao deseja realizar? digite 1 para soma, 2 para para subtraçao, 3 para multiplicao, 4 para a divisao"))


if(opcao == 1):
    numero1 = int(input("informe um numero"))
    numero2 = int(input("informe outro numero"))
    soma(numero1, numero2)

elif(opcao == 2):
    numero1 = int(input("informe um numero"))
    numero2 = int(input("informe outro numero"))
    subtraçao(numero1, numero2)

elif(opcao == 3):

    numero1 = int(input("informe um numero"))
    numero2 = int(input("informe outro numero"))
    multiplicacao(numero1, numero2)


elif(opcao == 4):
    numero1 = int(input("informe um numero"))
    numero2 = int(input("informe outro numero"))
    divisao(numero1, numero2)

else:
    print("entrada errada")

