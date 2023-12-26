# your_script.py

import os
import importlib
from flask import Flask, render_template, request, jsonify
from bots import chat_completion

app = Flask(__name__, template_folder='templates')

# Store API key in environment variable
os.environ['OPENAI_API_KEY'] = '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'


DEFAULT_BOT = 'chat_completion'

def select_bot():
    bot_module = importlib.import_module(f"bots.{DEFAULT_BOT}")
    return bot_module.generate_response  # Return the function for Flask to use








@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_bot_response', methods=['GET'])
def get_bot_response():
    user_input = request.args.get('user_input', '')
    bot_response = chat_completion.generate_response(user_input)
    return jsonify({'bot_response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
