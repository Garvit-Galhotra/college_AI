import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from response_generator import generate_response
from flask import Flask, request, jsonify
from Intent_classification import intent_prediction
from views import views  # Importing views.py

# Initialize Flask app
app = Flask(
    __name__,
    static_folder='../Frontend/static',  # Path to static files
    template_folder='../Frontend/templates'  # Path to templates folder
)

# Register the views blueprint
app.register_blueprint(views)

# API route for chatbot communication
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    # Predict the intent and get the bot's response
    intent = intent_prediction(user_message)
    bot_response = generate_response(intent)

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
