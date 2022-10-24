from flask import Flask, render_template, redirect , request, session

app = Flask(__name__)
app.secret_key = "Call me maybe"

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def submit_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def show_result():
    return render_template('result.html')
if __name__ == "__main__":
    app.run(debug=True)