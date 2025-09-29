#Letra A

# ex 1 - Falar o nome
def Falar_nome(nome):
    print(f"Olá {nome}")
    
# ex 2 - Somar dois numeros
def Soma_numero(n1, n2):
    soma = n1 + n2
    print(f"A soma de {n1} + {n2} é {soma}")

# ex 3 - Media de tres numeros
def Media_numeros(numero1,numero2,numero3):
    soma = numero1 + numero2 + numero3
    media = soma / 3
    print(f"A media dos numeros: {numero1}, {numero2} e {numero3} é: {media:.2f}")

# ex 4 - Medir a area do raio
def Medir_raio(raio):
    area = 3.14159 * (raio ** 2 )
    print (f"A aréa do raio de {raio} é {area}")

#Letra B
# ex 5 - Par ou impar
def Par_Impar(num):
    if num % 2 == 0:
        print(f"o Numero {num} é Par")
        return
    else:
        print(f"o Numero {num} é Impar")
        return "Impar"

# ex 6 - media do aluno
def Media_Aluno(n1, n2, n3, n4):
    soma = n1 + n2 + n3 + n4
    media = soma / 4
    if media >= 7:
        print(f"A media do aluno é {media:.2f} e ele está Aprovado ")
    elif media < 7 and media >= 5:
        print(f"A media do aluno é {media:.2f} e ele está de recuperação") 
    else:
        print(f"A media do aluno é {media:.2f} e ele está Reprovado")
    return media

# ex 7 - maior numero
def Max_numero(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print(f"O maior numero é {n1}")
    elif n2 >= n1 and n2 >= n3:
        print(f"O maior numero é {n2}")
    else:
        print(f"O maior numero é {n3}")
    return

# ex 8 - ano bissexto
def Ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} não é bissexto")
    return ano

#Letra C
# ex 9 - contagem regressiva
def Contagem_Regressiva(n):
    if n < 0:
        print("Contagem regressiva encerrada!")
    else:
        print(n)
        Contagem_Regressiva(n - 1)

# ex 10 - adivinhar a senha
def Adivinhar_senha(senha_correta):
    tentativas = 3
    while tentativas > 0:
        senha = input("Digite a senha: ")
        if senha == senha_correta:
            print("Acesso concedido!")
            return
        else:
            tentativas -= 1
            print(f"Senha incorreta. Você tem {tentativas} tentativas restantes.")
            if tentativas == 0:
                print("Acesso negado. Número máximo de tentativas atingido.")
                return

# ex 11 - soma total   
def Soma_Total():
    soma = 0
    while True:
        entrada = input("Digite um número (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break
        try:
            numero = float(entrada)
            soma += numero
        except ValueError:
            print("Por favor, digite um número válido ou 'sair'.")
    print(f"A soma dos valores digitados é: {soma}")
    return soma

# ex 12 - adivinhar o numero    
def Adivinhar_numero(numero_certo):
    tentativas = 5
    while tentativas > 0:
        try:
            palpite = int(input("Digite seu palpite: "))
            if palpite == numero_certo:
                print("Parabéns! Você adivinhou o número.")
                return
            elif palpite < numero_certo:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")
            tentativas -= 1
            print(f"Você tem {tentativas} tentativas restantes.")
        except ValueError:
            print("Por favor, digite um número válido.") 
    print(f"Suas tentativas acabaram. O número correto era {numero_certo}.")    
    return

#Letra D
#ex 13 - Tabuada
def Tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    return

# ex 14 - Contar vogais
def Contar_vogais(s):
    vogais = "aeiouAEIOU"
    contador = sum(1 for char in s if char in vogais)
    print(f"A string '{s}' possui {contador} vogais.")
    return contador

# ex 15 - Multiplos de 3 até 100
def Multiplos_de_3_ate_100():
    multiplos = [i for i in range(1, 101) if i % 3 == 0]
    print("Múltiplos de 3 entre 1 e 100:", multiplos)
    return multiplos

# ex 16 - Fatorial
def Fatorial(n):
    if n < 0:
        print("Fatorial não definido para números negativos.")
        return None
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    print(f"O fatorial de {n} é {fatorial}.")
    return fatorial

#Letra E

# ex 17 - Media de 3 notas
def Media3(a, b, c):
    if a < 0 or b < 0 or c < 0:
        print("Números negativos não são permitidos.")
        return None
    else:
        media = (a + b + c) / 3
        print(f"A média de {a}, {b} e {c} é {media:.2f}")
        return media

# ex 18 - Verificar se é primo
def eh_primo(n):
    if n <= 1:
        print(f"{n} não é um número primo.")
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} não é um número primo.")
            return False
    print(f"{n} é um número primo.")
    return True

# ex 19 - Saudar usuário
def saudar(nome, curso):
    mensagem = f"Olá, {nome}! Bem-vindo(a) ao curso de {curso}."
    print(mensagem)
    return mensagem

# ex 20 - Sequência de Fibonacci
def fibonacci(n):
    if n <= 0:
        print("Por favor, insira um número positivo.")
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    print(f"Os {n} primeiros termos da sequência de Fibonacci são: {fib_sequence}")
    return fib_sequence

# Fim

    



    
