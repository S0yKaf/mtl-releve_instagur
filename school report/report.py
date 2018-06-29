import sys
from database import db_session, init_db, init_engine
from Student import Student

init_engine("sqlite:///schooldb.sqlite")
init_db()



def add_user():
    first_name = input("Ecrie ton first_name:")
    last_name = input("Ecrie ton last_name:")
    age = input("Ecrie ton age:")
    email = input("Ecrie ton email:")

    new_student = Student(first_name, last_name, age, email)

    db_session.add(new_student)
    db_session.commit()

# db_session.delete(eleve);
def remove_user():
    students = Student.query.filter().all()
    for student in students:
        student.print_self()

    email_remove = input("Ecrie le email de la personne que tu veut supprimer:")
    student_delete = None

    for student in students:
        if student.email == email_remove:
            db_session.delete(student)
    db_session.commit()


def print_users():
    students = Student.query.filter(Student.is_expelled == False).all()
    for student in students:
        student.print_self()



def expell_student():
    students = Student.query.filter().all()
    for student in students:
        student.print_self()

    email_expell = input("Ecrie l'email de la personne que tu veut expulser:")


    students = Student.query.filter(Student.email == email_expell).first()
    print(students)

    student.expell()
    db_session.add(students)
    db_session.commit()


print()

user_input = ""
print('Bienvenue au System de gestion de l\'ecole lambda!')
while(user_input != 'exit'):
    print('a - ajouter un éleve.')
    print('b - supprimer un éleve.')
    print('c - afficher les éleves.')
    print("d - expulser un éleve. ")
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
