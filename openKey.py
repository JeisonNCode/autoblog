import openai
import json
import openai

def validarOpenAI():
    
    
    api_key = input("Escribe la API key de Open AI: ")

    openai.api_key = api_key

    try:
        response = openai.Completion.create(engine='text-davinci-003', prompt='Hola', max_tokens=5)
        if response['id']:
            print("La API key es válida.")
            with open('api_key.json', 'w') as file:
                    json.dump(api_key, file)
            validado=True
        else:
            print("La API key no es válida.")
    except openai.error.AuthenticationError:
        print("Error de autenticación: la API key no es válida. Vuelve a intentar o busca en OpenAI: https://platform.openai.com/docs/api-reference/")
        validado=False
    
    return validado
