from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    print('Екзаменаційна робота студенки МІТ-31 Радивоненко Анастасії')

if __name__ == '__main__':
    app.run(debug=True)