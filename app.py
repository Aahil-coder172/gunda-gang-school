from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace this with your actual Google Apps Script Web App URL
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwm6WglZUrtetkIf2Lcq3U9ch9Y_00PNr_LiIFxyxhLXV7E2KfkyLTdWgW7IELFvoqiIw/exec"

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

        # Prepare data for Google Sheets
        data = {
            "name": name,
            "code_name": code_name
        }

        try:
            response = requests.post(GOOGLE_SCRIPT_URL, json=data)
            if response.status_code == 200:
                return render_template('thankyou.html', code_name=code_name)
            else:
                return f"<h1>Error!</h1><p>Failed to save to Google Sheets: {response.text}</p>"
        except Exception as e:
            return f"<h1>Error!</h1><p>{e}</p>"

    return render_template('join.html')

@app.route('/downloads')
def downloads():
    return render_template('downloads.html')

if __name__ == '__main__':
    app.run(debug=True)
