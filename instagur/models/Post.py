from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper

from database import metadata, db_session


class Post:
    query = db_session.query_property()

    def __init__(self, filename, story, data_type):
        self.filename = filename
        self.story = story
        self.data_type = data_type

    def __repr__(self):
        return f'<Post {self.filename}>'


posts = Table('urls', metadata,
              Column('id', Integer, primary_key=True),
              Column('filename', String(2048), unique=True),
              Column('story', String, unique=False),
              Column('data_type', String(7), unique=False),
              Column('likes', Integer, unique=False)
              )

mapper(Post, posts)
