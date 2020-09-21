homiQuantidade = 0
muieQuantidade = 0
homiIdade = 0
muieIdade = 0
homiIdade1 = 0
muieIdade1= 0
Geral = 0
for x in range(10):
    genero = input("Insira o sexo da pessoa (homem ou mulher): ")
    if genero.lower() == "homem":
        homiQuantidade = homiQuantidade + 1
        homiIdade = float(input("Insira a idade da pessoa: "))
        homiIdade1 = homiIdade1 + homiIdade
    if genero.lower() == "mulher":
        muieQuantidade = muieQuantidade + 1
        muieIdade = float(input("Insira a idade da pessoa: "))
        muieIdade1 = muieIdade1 + muieIdade
homiTotal = homiIdade1/homiQuantidade
muieTotal = muieIdade1/muieQuantidade
Geral = (muieIdade1 + homiIdade1)/10
print("Idade media das mulheres: ", muieTotal)
print("Idade media dos homens: ", homiTotal)
print("A idade media do grupo é: ", Geral)

