import os
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Jenkins Test App'


if __name__ == '__main__':
    app.run()