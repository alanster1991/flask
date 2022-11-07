from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'This is not safe'

@app.route('/')
def count():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
