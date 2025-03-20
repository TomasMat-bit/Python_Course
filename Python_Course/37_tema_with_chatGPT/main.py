from http.client import responses

# from openai import OpenAI
#
# def chat_with_open_ai(api_key, prompt, model='gpt-4', temperature=0.7, max_tokens=30):
#     client = OpenAI(api_key=api_key)
#
#     response = client.chat.completions.create(
#         model=model,
#         messages=[{'role': 'user', 'content': prompt}],
#         max_tokens=max_tokens
#     )
#
#     return response
#
# api_key = ''
# prompt = 'Hello, how are you?'
#
# res = chat_with_open_ai(api_key, prompt)
#
# print(res)


from openai import OpenAI, api_key


def generate_image(api_key, prompt, size='1024x1024'):
    client = OpenAI(api_key=api_key)

    responses = client.images.generate(
        model='dall-e-2',
        prompt=prompt,
        size=size,
        n=1,
    )

    return responses.data[0].url

api_key = ''
prompt = 'A futuristic city in sunset'

image_url = generate_image(api_key, prompt)
print(image_url)
