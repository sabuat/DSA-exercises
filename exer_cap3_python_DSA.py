    # Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
    # depois faça uma chamada à função para listar os números

def pares():
    for i in range(1,21,2):
        print(i)

pares()

    # Exercício 2 - Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
    # Faça uma chamada à função, passando como parâmetro uma string

def mayus(a):
    a = a.upper()
    print (a)

mayus("rojito")

    # Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
    # imprima a lista

a = [6,7, 9, 13]
def add_list(b):
    a.append(b)
    print(a)

add_list(5)
add_list(1)

        # Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
        # à função, com apenas 1 elemento e na segunda chamada com 4 elementos

# def formalfun(arg1, *capa):
#     print(arg1)
#     for i in capa:
#         print(i)

formalfun(100)
formalfun(1,4,5)

        #Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
        # números como parâmetro e retornar a soma deles

soma = lambda x, y: x + y
print (soma(2,3))

        # Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
        # Crie uma função anônima que converta cada temperatura para Fahrenheit
        # Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
        # (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
        # Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x :(x * 9/5) + 32, Celsius)
print (list(Fahrenheit))

import pandas as pd



 

