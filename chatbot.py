from llama_cpp import Llama
import time

llm = Llama(model_path='models/ggml-vicuna-13b-4bit-rev1.bin')
keep_prompting = True
while keep_prompting:
    print('\n')
    prompt = input("What is your question? Type exit if done!! \n")
    if prompt.lower() == 'exit':
        keep_prompting = False
        break
    else:
        output = llm(prompt, temperature=0.7, top_p=1, max_tokens=499)
        choices = output['choices']
        for choice in choices:
            if 'Assistant' in choice['text']:
                assistant_response = choice['text'].split('Assistant:')[1].strip()
                if '###' in assistant_response:
                    assistant_response = assistant_response[:assistant_response.find('#')]
                for char in assistant_response:
                    print(char, end='', flush=True)
                    time.sleep(0.05)  # Adjust the sleep duration to control the speed of character display
                break
