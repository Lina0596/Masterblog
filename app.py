from crypt import methods

from flask import Flask, render_template, request, redirect, url_for
import json



blog_posts = [
                {'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
                {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.'},
             ]

json_blog_posts = json.dumps(blog_posts, indent=4)
with open ("blog_posts.json", "w") as json_file:
    json_file.write(json_blog_posts)



app = Flask(__name__)

@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    with open("blog_posts.json", "r") as json_file:
        blog_posts = json.loads(json_file.read())
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        with open("blog_posts.json", "r") as json_file:
            blog_posts = json.loads(json_file.read())
        new_author = request.form.get("author")
        new_title = request.form.get("title")
        new_content = request.form.get("content")
        blog_posts.append({"id": len(blog_posts) + 1, "author": new_author, "title": new_title, "content": new_content})
        new_blog_posts = json.dumps(blog_posts, indent=4)
        with open("blog_posts.json", "w") as json_file:
            json_file.write(new_blog_posts)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:post_id>', methods=['GET'])
def delete(post_id):
    with open("blog_posts.json", "r") as json_file:
        blog_posts = json.loads(json_file.read())
    for i in range(len(blog_posts)):
        if post_id == blog_posts[i]["id"]:
            del blog_posts[i]
            new_blog_posts = json.dumps(blog_posts, indent=4)
            with open("blog_posts.json", "w") as json_file:
                json_file.write(new_blog_posts)
            return redirect(url_for('index'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    #app.run(host="0.0.0.0", port=5000, debug=True)