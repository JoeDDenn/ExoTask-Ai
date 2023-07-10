from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("declare-lab/flan-alpaca-large")
model = AutoModelForSeq2SeqLM.from_pretrained("declare-lab/flan-alpaca-large")


def get_answer(input_text):
    # Tokenize your prompt text
    inputs = tokenizer.encode(input_text, return_tensors="pt")

    # Generate a response using the model
    outputs = model.generate(inputs, max_length=128)
    
    # Decode and print the generated output
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return output_text.strip()

