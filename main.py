# Comando input(): quero permitir que o usuário digite algo...
nome = input("Digite seu nome: ")

# Pede a idade para o usuário "Qual sua idade?"
idade = int(input("Qual sua idade? "))

# Comando de saída.. exibir na tela
print(f"Boa noite, seu nome é {nome}")

# Exiba "Sua idade é ..."
print("Sua idade é {}".format(idade))

# E se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))