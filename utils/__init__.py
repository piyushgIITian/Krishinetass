from flask import Flask,render_template

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = "developement"
app.config['FLASK_APP'] = "run.py"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if app.config['FLASK_ENV'] == "developement":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:killermb@localhost/flask_db'
else:
    app.config['DEBUG'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gzkhpoxkaklhmx:642b6b418b5d4d292305fa73c581c763fc231fcd1de48b8ad503c865bcf2c44d@ec2-52-3-60-53.compute-1.amazonaws.com:5432/d6o7p3cjt14apn'



@app.route("/")
def home():
    return render_template('main.html')

import posts
import weather