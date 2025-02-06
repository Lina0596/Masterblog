from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)


@app.route('/')
def index():
    with open("blog_posts.json", "r") as json_file:
        blog_posts = json.loads(json_file.read())
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        with open("blog_posts.json", "r") as json_file:
            blog_posts = json.loads(json_file.read())
        max_id = max([post["id"] for post in blog_posts], default=0)
        new_id = max_id + 1
        new_author = request.form.get("author")
        new_title = request.form.get("title")
        new_content = request.form.get("content")
        blog_posts.append({"id": new_id, "author": new_author, "title": new_title, "content": new_content})
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


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    with open("blog_posts.json", "r") as json_file:
        blog_posts = json.loads(json_file.read())
    for i in range(len(blog_posts)):
        if post_id == blog_posts[i]["id"]:
            post = blog_posts[i]
    if post is None:
        return "Post not found", 404
    if request.method == 'POST':
        updated_author = request.form.get("author")
        updated_title = request.form.get("title")
        updated_content = request.form.get("content")
        post["author"] = updated_author
        post["title"] = updated_title
        post["content"] = updated_content
        updated_blog_posts = json.dumps(blog_posts, indent=4)
        with open("blog_posts.json", "w") as json_file:
            json_file.write(updated_blog_posts)
        return redirect(url_for('index'))
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)