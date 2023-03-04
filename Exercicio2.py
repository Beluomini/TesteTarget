def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
  
def main(n):
    cont = 0
    vef = 0
    while(fibonacci(cont) <= n):
        if fibonacci(cont) == n:
            vef = n
        cont += 1
    if vef > 0:
        print("O número", n, "é um número de Fibonacci")
    else:
        print("O número", n, "não é um número de Fibonacci")

main(45)