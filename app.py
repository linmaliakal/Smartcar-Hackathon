from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('www/index.html')

if __name__ == '__main__':
    my_awesome_app.run()
#if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
