from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    #n - число послідовності, я обрала 3
    n = 3 
    #перший член арифметичної прогресії
    a1 = 1
    #другий 
    a2 = 2 
    #d - різниця
    d = a2 - a1
    result = sumOfAP(a1, d, n)
    return f'''
    <header>Екзаменаційна робота студенки МІТ-31 Радивоненко Анастасії. Білет№7</header>
    <p>Написати програму обчислення суми перших н членів арифметичної прогресії Х=1,2,3...<p>
    <p>
    <p>Сума перших н членів арифметичної прогресії: {result}
    '''

def  sumOfAP(a,  d,  n):
    sum = (n / 2) * (2 * a + (n - 1) * d)
    return sum

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')