from flask import Flask

app = Flask(__name__)


@app.route('/home')
def index():
    return 'Hello from Flask!'

if __name__ is "__main__":
  app.run()