api_key = "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"
import openai
import os
os.environ['openai_key'] = api_key
openai.api_key = os.environ['openai_key']
"""
keep_prompting = True
while keep_prompting:
    prompt = input("What is your question? Type exit if done!!\n")
    if prompt.lower() == 'exit':
        keep_prompting = False
    else:
        response = openai.Completion.create(engine='text-davinci-003', prompt= prompt,max_tokens=4000)
# for code model try to replace 'text-davinci-003' by 'code-davinci-002' to just output only code

    print(response['choices'][0]['text'])
"""

def get_answer(question):
    response = openai.Completion.create(engine='text-davinci-003', prompt= question,max_tokens=4000)
    return response['choices'][0]['text']