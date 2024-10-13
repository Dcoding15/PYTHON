import openai

API_KEY = ""
MODEL_NAME = ""

try:
    with open("data.json","w") as f:
        gpt = openai.OpenAI(api_key=API_KEY)
        prmpt = str(input('Enter message: '))
        output = gpt.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."},{'role':'user','content':prmpt}], model=MODEL_NAME, max_tokens=100, temperature=0.7)
        f.write(str(output))
except Exception as e:
    with open("data.json","w") as f:
        f.write(str(e))
