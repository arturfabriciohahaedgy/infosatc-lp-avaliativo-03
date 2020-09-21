mesDicionario = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho", 
    7: "Julho",
    8: "Agosto", 
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}
x = int(input("Insira um número (entre 1 e 12): "))
if x > 12:
    print("Numero maior que 12, favor iniciar o programa novamente.")
else: 
    print("O mês correspondente é: ", mesDicionario[x])