from flask import Flask

app = Flask(__name__)

@app.route('/clement')
def hello_world():
    return 'JOYEUX ANNIV LENNY'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
