def main():
    string = input("Digite uma string: ")
    strAux = ""
    for i in range(len(string)):
        strAux += string[len(string) - i - 1]

    print(strAux)
  
main()