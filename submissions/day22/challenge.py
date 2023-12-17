from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = 'My Web App'
    user = 'Alice'
    return render_template('index.html', title=title, user=user)

if __name__ == '__main__':
    app.run()