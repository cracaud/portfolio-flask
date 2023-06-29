from flask import Flask, render_template

app = Flask(__name__)

DATA = [
    {
    'id': 1,
    'title': 'Tyrone Wallace - Gauthier Denis - Juhann Begarin - Aamir Simms - Jeremy Evans',
    'plus-minus': 57,
    'minutes': 157.56,
    'possessions': 345,
    'ORTG': 108.41,
    'DRTG': 96.35
    },
    {
    'id': 2,
    'title': 'Kyle Allman - Tyrone Wallace - Axel Toupane - Aamir Simms - Ismael Kamagate',
    'plus-minus': -17,
    'minutes': 80.53,
    'possessions': 187,
    'ORTG': 98.40,
    'DRTG': 114.86
    },
    {
    'id': 3,
    'title': 'Tyrone Wallace - Gauthier Denis - Juhann Begarin - Aamir Simms - Ismael Kamagate',
    'plus-minus': -27,
    'minutes': 60.17,
    'possessions': 141,
    'ORTG': 102.13,
    'DRTG': 127.61
    },
    {
    'id': 4,
    'title': 'Kyle Allman - Axel Toupane - Juhann Begarin - Aamir Simms - Ismael Kamagate',
    'plus-minus': -17,
    'minutes': 55.44,
    'possessions': 124,
    'ORTG': 90.32,
    'DRTG': 101.56
    },
    {
    'id': 5,
    'title': 'Kyle Allman - Tyrone Wallace - Axel Toupane - Aamir Simms - Jeremy Evans',
    'plus-minus': 13,
    'minutes': 43.18,
    'possessions': 90,
    'ORTG': 101.11,
    'DRTG': 83.87
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', data=DATA)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)