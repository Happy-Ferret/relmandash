from __future__ import with_statement
from flask import Flask, request, session, g, redirect, url_for, \
     render_template, _app_ctx_stack
from dashboard.utils import *
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import timedelta
import os, site
from config import *

my_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))).split('/relmandash')[0]
site.addsitedir(my_dir)
site.addsitedir(os.path.join(my_dir, "bztools/bugzilla"))
site.addsitedir(os.path.join(my_dir, "remoteobjects"))

from utils import *

# configuration
DEBUG = True
SECRET_KEY = 'development key'

# create our little application :)
app = Flask(__name__)

app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['PROPAGATE_EXCEPTIONS'] = True

db_conn = DB_URL
app.config['SQLALCHEMY_DATABASE_URI'] = db_conn
db = SQLAlchemy(app)

app.permanent_session_lifetime = timedelta(minutes=60*3)

from dashboard.products import ComponentsTracker

def init_db():
    """Creates the database tables."""
    db.drop_all()
    db.create_all()
    ct = ComponentsTracker()

@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database again at the end of the request."""

app.jinja_env.globals.update(getTrackedBugs=getTrackedBugs)
app.jinja_env.globals.update(getAssignedBugs=getAssignedBugs)
app.jinja_env.globals.update(getUnassignedBugs=getUnassignedBugs)
app.jinja_env.globals.update(getProdCompBugs=getProdCompBugs)
app.jinja_env.globals.update(getNeedsInfoBugs=getNeedsInfoBugs)
app.jinja_env.globals.update(getToFollowBugs=getToFollowBugs)
app.jinja_env.globals.update(getToNominateBugs=getToNominateBugs)
app.jinja_env.globals.update(getToApproveBugs=getToApproveBugs)
app.jinja_env.globals.update(getToUpliftBugs=getToUpliftBugs)
app.jinja_env.globals.update(getKeywords=getKeywords)
app.jinja_env.globals.update(getComponents=getComponents)

if __name__ == '__main__':
    init_db()
    app.run()
    
from relmandash.models import *
import views_account
