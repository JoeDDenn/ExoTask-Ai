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

