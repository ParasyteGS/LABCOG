from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('details.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
