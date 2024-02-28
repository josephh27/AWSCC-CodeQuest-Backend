from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost:3306/crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Credential(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(255), nullable=False, unique=False)
    email = db.Column(db.String(255), nullable=False, unique=False)
    password = db.Column(db.String(255), nullable=False, unique=False)

    def __init__(self, website, email, password):
        self.website = website
        self.email = email
        self.password = password

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    distinct_websites = Credential.query.with_entities(Credential.website).distinct()
    credential_bucket = {}
    for website in distinct_websites:
        fetched_credentials = Credential.query.filter(Credential.website == website[0]).all()
        credential_bucket[website[0]] = fetched_credentials

    return render_template("index.html", credentials = credential_bucket)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        website = request.form['website']   
        email = request.form['email']   
        password = request.form['password']   

        my_data = Credential(website, email, password)
        db.session.add(my_data)
        db.session.commit()
        
        flash("Credential Inserted Successfully")

        return redirect(url_for('index'))
    
@app.route('/udpate', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Credential.query.get(request.form.get('id'))

        my_data.website = request.form['website']
        my_data.email = request.form['email']
        my_data.password = request.form['password']

        db.session.commit()
        flash("Credential Updated Successfully")

        return redirect(url_for('index'))
    
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Credential.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Credential Deleted Successfully")

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

