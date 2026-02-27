print("==================Exercicio 1=========================")
distancia_sp = {"Belo Horizonte": 490,"Curitiba": 339,"Porto Alegre": 852,"Salvador": 1454}
print(distancia_sp.get("Curitiba"))
soma = 0
atual = 0
for m in distancia_sp.values():
    soma += m
    if atual < m:
        atual = m
print(soma)
print(atual)

print("==================Exercicio 2=========================")

conexoes_cidades = {
    "Porto Alegre": ["Florianópolis", "São Paulo"],
    "Florianópolis": ["Curitiba", "Porto Alegre"],
    "Curitiba": ["Florianópolis", "Rio de Janeiro", "São Paulo"],
    "São Paulo": ["Belo Horizonte", "Curitiba", "Porto Alegre", "Salvador"],
    "Rio de Janeiro": ["Belo Horizonte", "Cuiabá", "Curitiba"],
    "Belo Horizonte": ["Brasília", "Cuiabá", "São Paulo", "Rio de Janeiro"],
    "Brasília": ["Belo Horizonte", "Fortaleza"],
    "Salvador": ["Fortaleza", "São Paulo"],
    "Cuiabá": ["Belo Horizonte", "Manaus", "Rio de Janeiro"],
    "Fortaleza": ["Manaus", "Salvador", "Brasília"],
    "Manaus": ["Cuiabá", "Fortaleza"]
}

print(conexoes_cidades.get("Cuiabá"))
print("")

for i in conexoes_cidades.get("Cuiabá"):
    if i == "Rio de Janeiro":
        presente = True
    else:
        presente= False

if presente == True:
    print("O Rio de janeiro esta presente na rota de Cuiaba")
else:
    print("O Rio de janeiro não esta presente na rota de Cuiaba")
print("")
print("==================Exercicio 3=========================")

grafo = {
"Manaus": ["Cuiabá", "Fortaleza"],
"Fortaleza": ["Manaus", "Salvador", "Brasília"],
"Salvador": ["Fortaleza", "São Paulo"],
"Brasília": ["Belo Horizonte", "Fortaleza"],
"Belo Horizonte": ["Brasília", "Cuiabá", "São Paulo", "Rio de Janeiro"],
"Cuiabá": ["Belo Horizonte", "Manaus", "Rio de Janeiro"],
"Rio de Janeiro": ["Belo Horizonte", "Cuiabá", "Curitiba"],
"São Paulo": ["Belo Horizonte", "Curitiba", "Porto Alegre", "Salvador"],
"Curitiba": ["Florianópolis", "Rio de Janeiro", "São Paulo"],
"Florianópolis": ["Curitiba", "Porto Alegre"],
"Porto Alegre": ["Florianópolis", "São Paulo"]
}

print(grafo.get("Brasília"))

cont=0
for i in grafo.get("São Paulo"):
    cont+=1
print(f"São Paulo possui {cont} de conexoes")

for n in grafo.get("Porto Alegre"):

    if n == "Curitiba":
        presente = True
    else:
        presente = False

if presente == True:
    print("Porto Alegre esta conectado com rota de Curitiba")
else:
    print("Porto Alegre não esta conectado com rota de Curitiba")




