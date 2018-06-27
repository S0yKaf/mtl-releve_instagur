import sys
from database import db_session, init_db, init_engine
from Student import Student

init_engine("sqlite:///schooldb.sqlite")
init_db()

# default_student = Student("John", "Doe")
# db_session.add(default_student)
# db_session.commit()
#
# user = Student.query.filter().first()
# user = Student.query.filter().all()
# print()

user_input = ""
print('Bienvenue au System de gestion de l\'ecole lambda!')
while(user_input != 'exit'):
    print('a - ajouter un éleve.')
    print('b - supprimer un éleve.')
    print('c - afficher les éleves.')
    user_input = input('>')

    if user_input is 'a':
        add_user()

    if user_input is 'b':
        remove_user()

    if user_input is 'c':
        print_users()

    if user_input is 'd':
        expell_student()

exit()


def add_user():
    pass


def remove_user():
    pass


def print_users():
    pass


def expell_student():
    pass
