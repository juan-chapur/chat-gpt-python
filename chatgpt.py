import openai

openai.api_key = "tu-api-key"

while True:
    prompt = input("\nIntroduce una pregunta: \n")
    if prompt == "exit":
        break
    complection = openai.Completion.create(engine="text-davinci-003",prompt=prompt, max_tokens=2048)
    res = complection.choices[0].text
    print(res)