from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model_name = "dondosss/rubert-finetuned-ner"
# model_name = "Grpp/rured2-ner-mdeberta-v3-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

nlp = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple", device=0)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_text', methods=['POST'])
def submit_text():
    data = request.get_json()
    user_text = data.get('input_text')

    entities = nlp(user_text)

    highlighted_text = user_text

    for entity in sorted(entities, key=lambda x: x['start'], reverse=True):
        word = entity['word']
        start = entity['start']
        end = entity['end']

        highlighted_text = highlighted_text[:start] + f"<mark>{word}</mark>" + highlighted_text[end:]

    return highlighted_text

if __name__ == "__main__":
    app.run(debug=True)