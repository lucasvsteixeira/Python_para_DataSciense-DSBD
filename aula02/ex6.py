# Armazena o preço na variável 'preco' e substitui vírgula por ponto para conversão correta para float
preco = float(input('Digite o preço: ').replace(",","."))
print(f"Preço: R$ {preco:.2f}")
