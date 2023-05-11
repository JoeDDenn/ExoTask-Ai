from llama_cpp import Llama

llm = Llama(model_path='models/ggml-vicuna-13b-4bit-rev1.bin')
keep_prompting = True
while keep_prompting:
    prompt = input("What is your question? Type exit if done!! \n")
    if prompt.lower() == 'exit':
        keep_prompting = False
        break
    else:
        output = llm(prompt)
        print(output['choices'][0]['text'])

