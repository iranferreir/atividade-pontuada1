import os
os.system("Cls || Clear")

# Variáveis para armazenar os números
lista_numero=[]
QUANTIDADE_NUMERO=5
maior_numero=0
menor_numero=0
for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"digite o {i+1}º numero: "))
    lista_numero.append(numero)

# Processando cada número
def pares_impares(a):
    contudor_impar=0
    contudor_par=0
    for numero in a:
        if numero %2 == 0:
            contudor_par += 1
             
        else:
            contudor_impar +=1
    return contudor_impar, contudor_par,

contudor_impar, contudor_par = pares_impares(lista_numero)
def media(a):

    for numero in a:
        if numero %2 == a:
            soma = sum(lista_numero)
            media_impar = soma / contudor_par
        else:
            soma = sum(lista_numero)
            media_par = soma / contudor_impar
    return media_impar, media_par

media_par, media_impar = media(lista_numero)     

maior_numero = max(lista_numero)
menor_numero = min(lista_numero)

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {contudor_par}")
print(f"Quantidade de ímpares: {contudor_impar}")
print(f"Quantidade de positivos: ")
print(f"Quantidade de negativos: ")
print(f"Maior número: {maior_numero} ")
print(f"Menor número: {menor_numero} ")
print(f"Média dos números pares: {media_par}")
print(f"Média dos números ímpares: {media_impar}")
print(f"Média de todos os números: ")
print(f"Números na ordem inversa: ")