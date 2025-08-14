
print ("olá vamos calcular?")
print ("digite um número:")

num1 = float(input())


print ("agora, escolha qual operação desejada:")
print ("se deseja SOMAR digite: 1")
print ("se deseja SUBTRAIR digite: 2")
print ("se deseja MULTIPLICAR digite: 3")
print ("se deseja DIVIDIR digite: 4")
print ("se deseja POTÊNCIALIZAR digite: 5")
print ("se deseja fazer a RAIZ QUADRADA digite: 6")
print ("se deseja cacular a PORCENTAGEM digite: 7")

oper1 = int(input())

if oper1 == 1:
  print ("**Voçe escolheu a soma**")


if oper1 == 2:
  print ("Voçe escolheu a subtração")

if oper1 == 3:
  print ("Voçe escolheu a multiplicação")

if oper1 == 4:
  print ("Voçe escolheu a divisão")

if oper1 == 5:
  print ("Voçe escolheu a potenciação")

if oper1 == 6:
  print ("Voçe escolheu a raiz quadrada")

if oper1 == 7:
  print ("Voçe escolheu a porcentagem")

print ("digite o segundo valor:")

num2 = float(input())

if oper1 == 1:
    print ("o resultado é:",num1 + num2)

elif oper1 == 2:
    print ("o resultado é:",num1 - num2)

elif oper1 == 3:
    print ("o resultado é:",num1 * num2)

elif oper1 == 4:
    print ("o resultado é:",num1 / num2)

elif oper1 == 5:
    print ("o resultado é:",num1 ** num2)


elif oper1 == 6:
  print ("o resultado é:",num1 ** (1/2))

elif oper1 == 7:
  print ("o resultado é:",(num1 / 100)*num2)

