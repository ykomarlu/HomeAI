from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# bcyrpt object initialization

class Users(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(15), unique=False, nullable=False)

    def __repr__(self):
        return f"userName: {userName}, password: {password}"
    # basically this function acts as the to-string for the Users python object
    # helps with debugging

# make the db connection
# the way that the database connection is

@app.route('/')
def index():
    return render_template('index.html')

# basically this allows the app to run if the current
# file that is being run is the main file
if __name__ == "__main__":
    app.run(debug=True)