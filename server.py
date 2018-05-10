from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template("survey.html")

@app.route('/output', methods=['GET', 'POST'])
def output():
    name = request.form['name']
    email = request.form['email']
    lang = request.form['lang']
    comments = request.form['comments']
    return render_template('output.html', name=name, email=email, lang=lang, comments=comments)

app.run(debug=True)