#Declaramos las funciones Lambda
mxn = lambda x: x*20
usd = lambda x: x/20

#Convertimos pesos a dólares utilizando la función Lambda
valorMXN = int(input("Dame un valor en pesos: "))
valorUSD = int(usd(valorMXN))

print("El total en dólares es: "+ str(valorUSD) + " dólares americanos")

#Convertimos dólares a pesos utilizando la función Lambda
valorUSD = int(input("Dame un valor en dólares: "))
valorMXN = int(mxn(valorUSD))
print("El total en pesos es: "+ str(valorMXN) + " pesos mexicanos")

#¿Cómo sería sin Lambdas? Definamos una función para convertir a pesos a dólares.
def convertirDolares (valorMXN):
    dolares=valorMXN/20
    return dolares

valorMXN = int(input("Funcion - Dame un valor en pesos: "))
valorUSD = int(convertirDolares(valorMXN))
print("El total en dólares es: "+ str(valorUSD) + " dólares americanos")

#Fin del programa
