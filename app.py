# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🎉 Hello, this Flask app is running on the web!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
