# Meu primeiro programa em Python
# Tema: print, variáveis e tipos de dados

# 1. Exibindo uma mensagem na tela
print("Olá, mundo!")

# 2. Variáveis e tipos de dados
nome = "Robson"        # str   (texto)
modulos = 6            # int   (número inteiro)
versao = 3.12          # float (número decimal)
estudando = True       # bool  (verdadeiro ou falso)

print(f"Meu nome é {nome}.")
print(f"Estou estudando Python {versao} e meu plano tem {modulos} módulos.")
print(f"Estou estudando Python? {estudando}")

# 3. Descobrindo o tipo de uma variável
print(type(nome))
print(type(modulos))
print(type(versao))
print(type(estudando))

# 4. Recebendo dados do usuário
cidade = input("Em que cidade você mora? ")
print(f"Legal! Você mora em {cidade}.")
