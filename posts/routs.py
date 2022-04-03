
from utils import app

@app.route("/posts")
def posts():
    pass

@app.route("/postshome")
def allPosts():
    pass


@app.route("/posts/submit", methods=['GET','POST'])
def submit():
    pass
        
@app.route('/postshome/<int:page_num>')
def paginate():
    pass