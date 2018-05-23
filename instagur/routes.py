import os.path

from instagur import app as app
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
    pass


# get a specific post
@app.route('/post/<id>', methods=['GET'])
def get_post(id):
    pass


# create a new post
@app.route('/post', methods=['POST'])
def add_poss():
    pass


# add a like to a post
@app.route('/post/<id>/like', methods=['GET'])
def like(id):
    pass


# add a comment to a post
@app.route('/post/comment', methods=['POST'])
def comment():
    pass
