from Todas_As_Funcoes import Falar_nome, Soma_numero, Media_numeros, Medir_raio
from Todas_As_Funcoes import Par_Impar, Media_Aluno, Max_numero, Ano_bissexto,Contagem_Regressiva, Adivinhar_senha
from Todas_As_Funcoes import Soma_Total, Adivinhar_numero
from Todas_As_Funcoes import Tabuada, Contar_vogais, Multiplos_de_3_ate_100, Fatorial
from Todas_As_Funcoes import Media3, eh_primo, saudar, fibonacci



# A
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

# B
# ex 5
num = int(input("digite um numero: "))
Par_Impar(num)

# ex 6
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

Media_Aluno(n1,n2,n3,n4)

# ex 7
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))      
n3 = float(input("Digite o terceiro numero: "))
Max_numero(n1,n2,n3)

# ex 8
ano = int(input("Digite um ano: "))
Ano_bissexto(ano)

# C
# ex 9
n = int(input("Digite um numero para iniciar a contagem regressiva: ")) 
Contagem_Regressiva(n)


# ex 10
Adivinhar_senha("python123")

# ex 11
Soma_Total()

# ex 12    
Adivinhar_numero(42)

# D
# ex 13
n = int(input("Digite um número para ver a tabuada: "))
Tabuada(n)

# ex 14
s = input("Digite uma string: ")
Contar_vogais(s)

# ex 15
Multiplos_de_3_ate_100()

# ex 16
n = int(input("Digite um número para calcular o fatorial: "))
Fatorial(n)

# E
# ex 17
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
Media3(n1, n2, n3)

# ex 18
num = int(input("Digite um número para verificar se é primo: "))
eh_primo(num)

# ex 19
nome = input("Digite seu nome: ")
curso = input("Digite o nome do curso (ou pressione Enter para 'Python'): ")
saudar(nome, curso) 

# ex 20
n = int(input("Digite quantos termos da sequência de Fibonacci você quer ver: "))
fibonacci(n)

# Fim do programa
