from flask import Flask, render_template, request, redirect, url_for, flash, session
import secrets
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex())

# Sample data
posts = [
    {'id': 1, 'title': 'First Post', 'content': 'This is my first post!'},
    {'id': 2, 'title': 'Flask Tips', 'content': 'Flask is a micro web framework for Python.'}
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'password':
            session['username'] = username
            flash('You were successfully logged in')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out')
    return redirect(url_for('index'))

# This is needed for Azure App Service
if __name__ == '__main__':
    # Use the PORT environment variable provided by Azure, or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
