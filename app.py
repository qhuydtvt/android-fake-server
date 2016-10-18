from flask import *
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app=app)

class HelloWorldApi(Resource):
    def get(self):
        return {"hello" : "world"}
    def post(self):
        json = request.get_json()
        print(json)
        return {"code" : 1, "message": "OK"}

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

api.add_resource(HelloWorldApi, '/')

def add(post):
    post["id"] = len(posts)
    posts.append(post)

if __name__ == '__main__':
    app.run()
