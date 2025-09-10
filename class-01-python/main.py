# Tipos Primitivos

print("Teste!")

name = "Emanuel"
num = 123
num2 = 12.6
is_active = True

print(name)
print(2134)
print(num)
print(num2)
print(is_active)

# Tipos estruturados

names = ["Carlos", "Ant Carlos", "Emanuel", "Jhyken"]

print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[-1])

user =  {
  "name": "Carlos",
  "age": 19,
  "position": "Lateral Esquerdo",
  "profession":"Jogador de Futebol",
  "is_active": True 
}

user2 =  {
  "name": "Thiago",
  "age": 19,
  "position": "Volante",
  "profession":"Jogador de Futebol",
  "is_active": True 
}

user3 =  {
  "name": "João Paulo",
  "age": 29,
  "position": "Nas duas",
  "profession":"Jogador de Futebol",
  "is_active": True 
}

print(user)
print(user["name"])
print(user["age"])

def sum(num1, num2):
  sum = num1 + num2
  return sum

result = sum(2, 5)
print(result)

print("Gato" + " Preto")
print(user["name"] + ": " + user["profession"])

def say_user(user):
  result = user["name"] + ": " + user["position"]
  return result

message = say_user(user)
print(message)

message2 = say_user(user2)
print(message2)

# input/output

# name_user = input("Digite seu nome: ")
# print("Olá, " + name_user)

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))

# print(type(num1))
# result = num1 + num2

# print("Resultado: " + str(result))

# conditionals

print(1!=1)
print(1==1)
print(1>1)

if (1!=1):
  print("Verdadeiro")
else:
  print("Falso")

# user_age = int(input("Digite sua idade: "))
 
# if ( user_age >= 18):
#   print("Maior de idade")
# else:
#   print("Menor de idade")


# loops

for i in range(1, 1001):
  print(i)

for name in names:
  print(name)


players = [user, user2, user3]

for player in players:
  if (player["age"] <= 20):
    print(player["name"])

for player in players:
  if (player["position"] == "Nas duas"):
    print(player["name"])
