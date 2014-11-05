__author__ = 'dmaust'

from flask import Flask, render_template, request
import time
app = Flask(__name__)

@app.route('/')

def hello_world():
    return render_template('index.html', hello=time.time())

@app.route('/test')
def test():
    return 'mytest'

@app.route('/add', methods=['post'])
def add():
    print "Running add"
    print request.form
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    return render_template("add_result.html", answer=(num1 + num2))

if __name__ == '__main__':
    app.run(debug=True)