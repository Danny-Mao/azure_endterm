from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('form.html')

@app.route('/aml')
def aml():
    

@app.route('/about')
def about():
    return 'About'

if __name__=="__name__":
    app.run()