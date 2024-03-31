from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/hot')
def hot():
    return render_template_string("<body style='background-color: red;'>Hot</body>")

@app.route('/cold')
def cold():
    return render_template_string("<body style='background-color: blue;'>Cold</body>")

@app.route('/')
def index():
    return render_template_string("<body style='background-color: green;'>Index</body>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)