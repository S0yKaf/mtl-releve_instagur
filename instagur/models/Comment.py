from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper

from instagur.database import metadata, db_session


class Comment:
    query = db_session.query_property()

    def __init__(self, post_id, author, comment):
        self.post_id = post_id
        self.author = author
        self.comment = comment

    def __repr__(self):
        return '<User %r>' % (self.username)


comments = Table('comment', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('post_id', Integer, unique=False),
                 Column('author', String(255), unique=False),
                 Column('comment', String(255), unique=False)
                 )

mapper(Comment, comments)
