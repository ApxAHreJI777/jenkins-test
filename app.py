import os
from flask import Flask

s = os.environ.get('APP_MSG')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return f'Jenkins Test App: {s}'


if __name__ == '__main__':
    app.run()