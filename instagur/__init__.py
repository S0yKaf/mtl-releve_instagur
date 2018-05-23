from flask import Flask
app = Flask(__name__)

from instagur import routes  # noqa I'm sorry pep8
