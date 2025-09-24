from openai import OpenAI

API_KEY=""

client = OpenAI(api_key=API_KEY)

print("\n========== Assistente Virtual do Reprograma Jucás ==========\n")
print("🤖 Bot: Como posso ajudar?")

messages = [
  {"role": "system", "content": "Você é um assistente chamado Reprograma"}
]

while True:
    message = input("🙂 You: ")
    if message.lower() in ["sair", "parar", "encerrar"]:
      print("🤖 Bot: Obrigado volte sempre!")
      break
    else:
      messages.append({"role": "user", "content": message})
      
      response = client.responses.create(
        model="gpt-4.1-mini", 
        input=messages
      )
      
      print(f"🤖 Bot: {response.output[0].content[0].text}")