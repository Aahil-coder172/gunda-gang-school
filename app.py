
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form['name']
        code_name = request.form['code_name']
        
        with open('members.txt', 'a') as f:
            f.write(f"Name: {name}, Code Name: {code_name}\n")
        
        return f"<h1>Welcome to the gang, {code_name}!</h1><p><a href='/'>Go back</a></p>"
    return render_template('join.html')

@app.route('/downloads')
def downloads():
    return render_template('downloads.html')

if __name__ == '__main__':
    app.run(debug=True)
