from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    n = 5
    a1 = 2
    a2 = 4
    d = a2 - a1
    result = sumOfAP(a1, d, n)
    return f'''
    <header>Екзаменаційна робота студенки МІТ-31 Радивоненко Анастасії</header>
    <p>Написати програму обчислення суми перших н членів арифметичної прогресії Х=2,4,6<p>
    <p>Сума перших н членів арифметичної прогресії: {result}
    '''

def  sumOfAP(a,  d,  n):
    sum = (n / 2) * (2 * a + (n - 1) * d)
    return sum

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')