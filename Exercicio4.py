def main():
    estados = ["SP", "RJ", "MG", "ES", "Outros"]
    faturamentos = [ 67836.43, 36678.66, 29229.88, 27165.48, 19849.53 ]

    faturamentoTotal = sum(faturamentos)
    for i in range(len(estados)):
        print("O faturamento do estado de", estados[i], "foi de R$", faturamentos[i], "representando", faturamentos[i] / faturamentoTotal * 100, "% do faturamento total")

main()