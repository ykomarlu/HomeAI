from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class name(db.Model):
    id = db.Column(db.Integer, primary_key=True  )

# make the db connection
# the way that the database connection is

@app.route('/')
def index():
    return render_template('index.html')

# basically this allows the app to run if the current
# file that is being run is the main file
if __name__ == "__main__":
    app.run(debug=True)