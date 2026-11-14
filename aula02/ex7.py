nome, idade, cidade = input(
    "Digite nome, idade e cidade separados por espaço: "
).split() # Armazena os valores digitados pelo usuário nas variáveis 'nome', 'idade' e 'cidade'

idade = int(idade) # Converte a idade de string para inteiro

# Exibe o nome, idade e cidade do usuário usando f-string p/ formatação da saída
print(f"{nome} tem {idade} anos e mora em {cidade}.")