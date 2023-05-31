from flask import Flask, render_template, request
import unittest
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        p = request.form.get("num_1")
        r = request.form.get("num_2")
        n = request.form.get("num_3")
        t = request.form.get("num_4")
        return render_template('index.html',ans=calc(p,r,n,t))
    else:
        return render_template("index.html")
def calc(p,r,n,t):
    try:
        p = float(p)
        r = float(r)
        n = float(n)
        t = float(t)
    except ValueError:
        return 'ValueError: не является числом'
    except TypeError:
        return "TypeError: недопустимое значение"
    if (p < 0 or r < 0 or n < 0 or t < 0):
        return "Одно или все значения меньше нуля"
    else:
        ans = int(p * (1 + (r / n)) ** (n * t))
        return ans

class test_Converter(unittest.TestCase):
    def test_values(self):
        self.assertEqual(calc(1000, 0.1, 2, 5), int(1628))
        self.assertEqual(calc(-1000, -0.1, -2, -5), "Одно или все значения меньше нуля")

    def test_types(self):
        self.assertEqual(calc(1000, 0.1, 2, "пять"), 'ValueError: не является числом')
        self.assertEqual(calc(1000, 0.1, 2, [1, 2, 3]), 'TypeError: недопустимое значение')
        self.assertEqual(calc(1000, 0.1, 2, (1, 2, 3)), 'TypeError: недопустимое значение')



if __name__ == "__main__":
    app.run(debug=True)

