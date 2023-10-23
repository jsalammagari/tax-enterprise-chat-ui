#from flask import Flask, request, jsonify, send_from_directory
from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__, static_url_path='', static_folder='.')

OPENAI_API_URL = 'https://api.openai.com/v1/engines/davinci/completions'
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

TAX_KEYWORDS = ['tax', 'deduction', 'income', 'IRS', 'refund', 'W-2', '1040', 'EIN', 'audit']

def is_tax_related(question):
    """Check if the question is related to taxes based on keywords."""
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in TAX_KEYWORDS)

# @app.route('/')
# def index():
#     return send_from_directory('.', 'index.html')
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question', '')
    
    # Check if the question is tax-related
    if not is_tax_related(question):
        return jsonify({'answer': "Your question doesn't seem related to taxes. Please ask a tax-related question."})
    
    answer = get_gpt_response(question)
    return jsonify({'answer': answer})

def get_gpt_response(question):
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'prompt': question,
        'max_tokens': 150
    }

    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    response_json = response.json()

    return response_json.get('choices', [{}])[0].get('text', '').strip()

if __name__ == '__main__':
    app.run(debug=True)
