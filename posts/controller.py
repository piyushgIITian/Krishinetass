from flask import request,render_template
from posts.models import Posts
from utils import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

@app.route("/posts")
def posts():
    return render_template('index.html')



@app.route("/posts/submit", methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        message = request.form['message']
        lat = request.form['lat']
        lon = request.form['lon']
        print("IMPORTANT:::",lat,lon,message)
        post = Posts(message,lat,lon)
        db.session.add(post)
        db.session.commit()

        
    return render_template('success.html',data=post)

@app.route("/postshome")
def allPosts():
    return render_template('posts.html',posts=db.engine.execute("SELECT * FROM posts Order By message ASC"))
    
     



@app.route('/postshome/<int:page_num>')
def paginate(page_num):
    records_per_page = 10
    offset = (page_num - 1) * records_per_page
    paginatedPosts = db.engine.execute(f"Select * from public.posts Order By message LIMIT {records_per_page} OFFSET {offset} ")
    return render_template('posts.html', posts=paginatedPosts)  