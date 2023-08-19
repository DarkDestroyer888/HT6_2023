from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return "Received form data: Name - {name}, Email - {email}"
    return render_template('index.html')  # Create an HTML template for the form

if __name__ == '__main__':
    app.run(debug=True,port=8080,host='127.0.0.1')
