# tax-enterprise-chat-ui
A web-based interface for users to ask tax-related questions. It uses the OpenAI GPT model to generate answers, ensuring users get detailed and relevant information.

Tax Questions Chat Interface

Project Structure
app.py: The backend Flask application.
templates\index.html: The frontend user interface.

Features
Tax Question Filtering: Ensures only tax-related questions are processed.
Integration with OpenAI GPT: Uses one of the most advanced language models to generate answers.

Running the Application
Set Flask app environment variables and run:

set FLASK_APP=app.py
set FLASK_ENV=development
flask run

Open a web browser and navigate to:

http://127.0.0.1:5000/

Usage

Enter your tax-related question in the provided text area.
Click "Ask" to get the answer.
If your question isn't recognized as tax-related, you'll be prompted to ask a tax-specific question.

The recording of the chat application usage can be accessed [here](https://drive.google.com/file/d/11e1gRNlQSVhUd0OmhEZAco9Z6bWgmDvX/view?usp=sharing)
