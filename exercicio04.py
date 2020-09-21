#Parte 1 do exercicio
i = 0 #segura o loop do For e do While
listaNome = []
listaCPF = []
listaSenha = []
listaDoador = []
while i != 1:
    idade = int(input("Insira sua idade: "))
    if idade < 16 or idade > 69:
        i = 2
        break
    peso = int(input("Insira seu peso: "))
    if peso > 50:
        i = 2
        break
    horarioSono = int(input("Insira quantas horas dormiu hoje (ultimas 24 horas): "))
    if horarioSono < 6:
        i = 2
        break
    i = 1

if i == 2:
    print("Você não esta apto para ser um doador")
if i == 1:
    print("Você esta apto para se tornar um doador de sangue, parabéns!")

#Parte 2 do exercicio 
oferta = input("Você gostaria de se cadastrar? ")
if oferta.lower() == "sim":
    for i in range(5): #Fiquei em duvida se era pro usuario botar os valores ou pra eu botar, então decidi por fazer um loop em while.
        nomeCompleto = input("Cadastre seu nome completo: ")
        listaNome.append(nomeCompleto)
        cpf = int(input("Cadastre seu CPF: "))
        listaCPF.append(cpf)
        senha = input("Cadastre sua senha: ")
        listaSenha.append(senha)
        doador = input("Você esta apto para ser um doador?")
        listaDoador.append(doador)
elif oferta.lower() == "nao" or "não":
        print("Voltar em outro horario")

for i in listaNome:
    print("Nome completo: ",i)
for i in listaCPF:
    print("CPF: ",i)
for i in listaSenha:
    print("Senha: ",i)
for i in listaDoador:
    print("É doador?: ",i)



