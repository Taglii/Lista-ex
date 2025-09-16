from part1 import Falar_nome
from part1 import Soma_numero
from part1 import Media_numeros
from part1 import Medir_raio

# ex 1
nome = input("Qual seu nome? ")
Falar_nome(nome)

# ex 2
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
Soma_numero(n1,n2)

# ex 3 
numero1 = float(input("digite o primeiro numero: "))
numero2 = float(input("digite o Segundo numero: "))
numero3 = float(input("digite o terceiro numero: "))
Media_numeros(numero1,numero2,numero3)

# ex 4 
raio = float(input("Digite o raio: "))
Medir_raio(raio)
