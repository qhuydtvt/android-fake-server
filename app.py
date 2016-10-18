import json
from flask import Flask, request

app = Flask(__name__)

post1 = {
    "id": 0,
    "title": "I met a girl",
    "content": "Today I met a girl, her name is Hanna. She got black eyes and loves ice-cream"
}

post2 = {
    "id": 1,
    "title": "Today is very good day",
    "content": "New chapter of One Piece was out"
}

post3 = {
    "id": 2,
    "title": "Class are fun",
    "content": "We learned new things everyday and we try hard"
}

posts = [post1, post2, post3] #Array

print(posts)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return json.dumps(posts)
    if request.method == "POST":
        title = request.get_json()["title"]
        content = request.get_json()["content"]
        post = {"title": title, "content": content}
        add(post)
        return json.dumps({"code": 1, "message": "OK"})

def add(post):
    post["id"] = len(posts)
    posts.append(post)

if __name__ == '__main__':
    app.run()
