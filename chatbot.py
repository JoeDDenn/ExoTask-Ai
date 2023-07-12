from transformers import pipeline

flag = True
while flag:
    prompt = input("write a prompt or exit to quit ")
    if prompt =='exit':
        flag = False
    else:
        model_name = "declare-lab/flan-alpaca-gpt4-xl"
        chatbot = pipeline("text2text-generation", model=model_name)
        print(chatbot(prompt)[0]["generated_text"])
