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

names = ["Marcos", "Ant Carlos", "Emanuel", "Jhyken"]

print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[-1])

user =  {
  "name": "Marcos",
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
