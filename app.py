from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for comments (for demonstration purposes)
comments = []

@app.route('/')
def index():
    return render_template('index.html', comments=comments)

@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    username = request.form['username']
    content = request.form['comment']
    comments.append({'username': username, 'content': content})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
