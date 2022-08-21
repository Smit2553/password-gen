from flask import Flask, render_template, request
from passwordgenerator import generate_random_password
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        options = request.form.getlist('mycheckbox')
        number = request.form.get('numberbox')
        password = generate_random_password(options, int(number))
        return render_template('index.html', password="".join(password))
    password = generate_random_password([], int(16))
    return render_template('index.html', password="".join(password))


if __name__ == '__main__':
    app.run()
