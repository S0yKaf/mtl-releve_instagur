from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy.orm import mapper
from database import metadata, db_session


class Student:
    query = db_session.query_property()
    def __init__(self, first_name, last_name, age=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def expell(self):
        self.is_expelled = True

    def print_self(self):
        print(self.first_name, self.last_name, self.age, self.email)

students = Table('student', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('first_name', String(100), unique=False),
                 Column('last_name', String(100)),
                 Column('age', String()),
                 Column('email', String(100), unique=True),
                 Column('is_expelled', Boolean, default=False)
                 )

mapper(Student, students)
