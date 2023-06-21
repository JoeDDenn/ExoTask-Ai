# api_key = "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"
# import openai
# import os
# os.environ['openai_key'] = api_key
# openai.api_key = os.environ['openai_key']
# # """
# # keep_prompting = True
# # while keep_prompting:
# #     prompt = input("What is your question? Type exit if done!!\n")
# #     if prompt.lower() == 'exit':
# #         keep_prompting = False
# #     else:
# #         response = openai.Completion.create(engine='text-davinci-003', prompt= prompt,max_tokens=4000)
# # # for code model try to replace 'text-davinci-003' by 'code-davinci-002' to just output only code

# #     print(response['choices'][0]['text'])
# # """

# def get_answer(question):
#     response = openai.Completion.create(engine='text-davinci-003', prompt= question,max_tokens=4000)
#     return response['choices'][0]['text']

# get_answer("What is the best programming language?")

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("declare-lab/flan-alpaca-large")
model = AutoModelForSeq2SeqLM.from_pretrained("declare-lab/flan-alpaca-large")

# Tokenize your prompt text
input_text = "what is AI?"
inputs = tokenizer.encode(input_text, return_tensors="pt")

# Generate a response using the model
outputs = model.generate(inputs, max_length=128)

# Decode and print the generated output
output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
# print(output_text)
# chatbot.py

def get_answer(input_text):
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    
    outputs = model.generate(inputs, max_length=128)
    
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return output_text.strip()