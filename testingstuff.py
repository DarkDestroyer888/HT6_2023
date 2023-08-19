from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        ifdrink = request.form['ifdrink']
        ifexercise = request.form['ifexercise']
        diet = request.form['diet']
        weight = request.form['weight']
        
        # You can process or store the data here as needed
        
        return "Received data: Name: {name}, Age: {age}, Water: {ifdrink}, Exercise: {ifexercise}, Diet: {diet}, Weight: {weight}"
    
    return render_template('form.html')  # Create a template for your HTML form

if __name__ == '__main__':
    app.run(debug=True)
    