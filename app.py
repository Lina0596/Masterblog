from flask import Flask, render_template
import json


"""
blog_posts = [
                {'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
                {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.'},
             ]

json_blog_posts = json.dumps(blog_posts, indent=4)
with open ("blog_posts.json", "w") as json_file:
    json_file.write(json_blog_posts)
"""

app = Flask(__name__)


@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    with open("blog_posts.json", "r") as json_file:
        blog_posts = json.loads(json_file.read())
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    #app.run(host="0.0.0.0", port=5000, debug=True)