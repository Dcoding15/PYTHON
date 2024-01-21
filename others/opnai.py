from openai import OpenAI

gpt = OpenAI(api_key='')	# Insert OpenAI api key

prmpt = str(input('Enter message: '))

output = gpt.chat.completions.create(messages=[{'role':'user','content':prmpt}], model='gpt-3.5-turbo-0613')

print(output.choices[0].message.content)
