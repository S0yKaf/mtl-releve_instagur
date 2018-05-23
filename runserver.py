import sys
from instagur import app
from instagur.database import db_session, init_db, init_engine

app.config.from_pyfile('../config/config.py')
if len(sys.argv) == 2:
    conf = sys.argv[1]
    print(f'Loading additional config {conf}')
    app.config.from_pyfile(f'config/{conf}')

init_engine(app.config['DATABASE_URI'])
init_db()
app.run(port=8080)
