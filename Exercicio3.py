import json

def menorValor(dias, valores):
    menor = valores[0]
    for i in range(len(valores)):
        if valores[i] < menor:
            menor = valores[i]
            dia = dias[i]
    return dia, menor

def maiorValor(dias, valores):
    maior = valores[0]
    for i in range(len(valores)):
        if valores[i] > maior:
            maior = valores[i]
            dia = dias[i]
    return dia, maior

def acimaMedia(valores):
    media = sum(valores) / len(valores)
    acima = 0
    for i in range(len(valores)):
        if valores[i] > media:
            acima += 1
    return acima

def main():
    dias = []
    valores = []

    with open('dados.json', 'r') as arquivo:
        dados = json.load(arquivo)
  
    for i in dados:
        dias.append(i['dia'])
        valores.append(i['valor'])
        
    print("O menor valor é do dia", menorValor(dias, valores)[0], "com o valor de R$", menorValor(dias, valores)[1])
    print("O maior valor é do dia", maiorValor(dias, valores)[0], "com o valor de R$", maiorValor(dias, valores)[1])
    print("Houveram", acimaMedia(valores), "de dias com o faturamento acima da media")

main()