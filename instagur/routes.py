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
    if filename and \
       not os.path.exists(f'{basename}/public/uploads/{filename}'):
        return send_file('public/404.html'), 404

    return send_from_directory('public/uploads/', filename)


# @app.route('/disconect', methods=['POST'])
# def disconect():
#     if app.config['SECRET_KEY'] != secret:



@app.errorhandler(404)
def page_not_found(e):
    return send_file('public/404.html'), 404

# POST ROUTES


# Get a list of all posts
@app.route('/post/all', methods=['GET'])
def get_all_posts():
    posts = Post.query.filter(Post.is_deleted == False).all() # filter pour pas aller chercher les is_deleted

    response = []
    for post in posts:
        response.append({
            "id": post.id,
            "filename": post.filename,
            "story": post.story,
            "data_type": post.data_type,
            "likes": post.likes,
            "created_at": post.created_at,
            "comments": get_post_comments(post.id)
        })
    return jsonify(response)


def get_post_comments(id):
    comments = Comment.query.filter(Comment.post_id == id).all()
    response = []
    for comment in comments:
        response.append({
            "id": comment.id,
            "author": comment.author,
            "comment": comment.comment
        })
    return response


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


@app.route('/post/<id>/<secret>', methods=['GET'])
def delete_post(id, secret):
    post = Post.query.filter(Post.id == id).first()

    if not post:
        print("ereure delete Poste apres code")
        return (f'no post with id {id}', 500)

    if app.config['SECRET_KEY'] == secret:

        post.is_deleted = True
        db_session.add(post)
        db_session.commit()
        print("delete Post")

    return "post Deleted!"


@app.route('/comment/<id>/<secret>', methods=['GET'])
def delete_comment(id, secret):
    comment = Comment.query.filter(Comment.id == id).first()
    if not comment:
       return (f'no comment with id {id}', 500)

    if app.config['SECRET_KEY'] == secret:
        db_session.delete(comment)

    db_session.commit()
    return "comment Deleted!"



# add a like to a post
@app.route('/post/<id>/like', methods=['POST'])
def like(id):
    post = Post.query.filter(Post.id == id).first()
    if not post:
        return (f'no post with id {id}', 500)

    post.likes += 1
    db_session.commit()
    return 'liked!'

# # add a comment to a post
# @app.route('/post/<id>/comments', methods=['POST'])
# def comment(id):
#     post = Post.query.filter(Post.id == id).first()
#     if not post:
#         return (f'no post with id {id}', 500)
#
#     post.coments += 1
#     db_session.commit()
#     return 'comment!'


@app.route('/post/<id>/comments', methods=['GET'])
def get_comments(id):
    comments = Comment.query.filter(Comment.post_id == id).all()
    response = []
    for comment in comments:
        response.append({
            "id": comment.id,
            "post_id": comment.post_id,
            "author": comment.author,
            "comment": comment.comment
        })
    return jsonify(response)


# add a comment to a post
@app.route('/post/<id>/comment', methods=['POST'])
def comment(id):
    req = request.get_json()
    print(req)
    if 'comment' not in req:
        return jsonify({'error': 'Bad request'}), 400

    comment = Comment(id, 'anon', req['comment'])
    db_session.add(comment)
    db_session.commit()
    return 'posted'
