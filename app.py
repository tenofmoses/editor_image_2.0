from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/posts_database"
mongo = PyMongo(app)

@app.route("/post/<post_id>")
def home_page(post_id):
    posts = mongo.db.posts.find({"post_id": post_id})
    return render_template("index.html",
        posts=posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0')