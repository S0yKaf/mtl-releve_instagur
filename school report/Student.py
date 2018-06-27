from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy.orm import mapper

from database import metadata, db_session


class Student:
    query = db_session.query_property()

    def __init__(self, first_name, last_name, age=None, email=None):
        self.first_name = first_name


    def print_self(self):
        pass

students = Table('student', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('first_name', String(100), unique=False),
                 Column('is_expelled', Boolean, default=False)
                 )

mapper(Student, students)
