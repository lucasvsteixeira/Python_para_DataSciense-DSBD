nome_aluno = 'Rocky' # Declaração de variável
idade_aluno = 15 # Declaração de variável
media_aluno = 8.45 # Declaração de variável

# Formatação de string com o operador %
print('Nome do aluno é %s, ele tem %d anos e sua média é %f.' %(nome_aluno, idade_aluno,media_aluno))

# Formatação de string com o operador % e nº de casas decimais
print('Nome do aluno é %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno, idade_aluno, media_aluno))

nome_aluno = "Daniel"
idade_aluno = 31
media_aluno = 10 

# Formatação de string com método format
print('Nome do aluno é {}, ele tem {} anos e sua média é {}.' .format(nome_aluno, idade_aluno, media_aluno))

# Formatação de string com f-string
print(f'Nome do aluno é {nome_aluno}, ele tem {idade_aluno} anos e sua média é {media_aluno}.')

# Formatação de string com f-string com numero de casas decimais
print(f'Nome do aluno é {nome_aluno}, ele tem {idade_aluno} anos e sua média é {media_aluno: .2f}.')
