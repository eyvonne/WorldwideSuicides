from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/datacleaning')
def cleaning():
    return render_template('cleaning.html')


@app.route('/modeling')
def models():
    return render_template('modeling.html')


@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run()
