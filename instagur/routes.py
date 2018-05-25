import os.path
import json

from instagur import app as app
from instagur.models.Post import Post
from instagur.models.Comment import Comment
from instagur.database import db_session
from flask import request, send_file, send_from_directory, jsonify, redirect

basename = os.path.dirname(__file__)

@app.route('/', methods=['GET'])
def index():
    return send_file('public/index.html')


@app.route('/<route>', methods=['GET'])
def page(route):
    if route and not os.path.exists(f'{basename}/public/{route}.html'):
        return send_file('public/404.html'), 404

    return send_file(f'public/{route}.html')


@app.route('/js/<filename>', methods=['GET'])
def javascript(filename):
    print(filename)
    if filename and not os.path.exists(f'{basename}/public/js/{filename}'):
        return send_file('public/404.html'), 404

    return send_from_directory('public/js/', filename)


@app.route('/css/<filename>', methods=['GET'])
def css(filename):
    if filename and not os.path.exists(f'{basename}/public/css/{filename}'):
        return send_file('public/404.html'), 404

    return send_from_directory('public/css/', filename)


@app.route('/uploads/<filename>', methods=['GET'])
def uploads(filename):
    if filename and not os.path.exists(f'{basename}/public/uploads/{filename}'):
        return send_file('public/404.html'), 404

    return send_from_directory('public/uploads/', filename)


@app.route('/login', methods=['POST'])
def login():
    pass


@app.errorhandler(404)
def page_not_found(e):
    return send_file('public/404.html'), 404

# POST ROUTES

# Get a list of all posts
@app.route('/post/all', methods=['GET'])
def get_all_posts():
    posts = Post.query.all()
    response = []
    for post in posts:
        response.append({
            "id": post.id,
            "filename": post.filename,
            "story": post.story,
            "data_type": post.data_type,
            "likes": post.likes,
            "created_at": post.created_at
        })
    return jsonify(response)


# get a specific post
@app.route('/post/<id>', methods=['GET'])
def get_post(id):
    pass


# create a new post
@app.route('/post', methods=['POST'])
def add_post():  # TODO REFACTOR THIS U FUK
    file = request.files['file']
    file_path = f'{basename}/public/uploads/{file.filename}'
    story = request.form['content']

    post = Post(file.filename, story, file.mimetype)
    db_session.add(post)
    db_session.commit()

    file.stream.seek(0)
    file.save(file_path)

    return f'{file.filename} uploaded succesfully!'


# add a like to a post
@app.route('/post/<id>/like', methods=['GET'])
def like(id):
    pass


# add a comment to a post
@app.route('/post/comment', methods=['POST'])
def comment():
    pass
