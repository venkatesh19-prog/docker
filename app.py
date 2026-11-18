
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Docker CI/CD using GitHub Actions is working!"

@app.route('/about')
def about():
    return "This is my first Dockerized Python application."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
