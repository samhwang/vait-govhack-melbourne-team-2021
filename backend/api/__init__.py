import os
from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app)

# Database configs
db_user = os.environ["POSTGRES_USER"]
db_password = os.environ["POSTGRES_PASSWORD"]
db_name = os.environ["POSTGRES_DB"]
db_host = os.environ["POSTGRES_HOST"]
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Default app routes
@app.route('/')
def hello_world():
    return 'Hello!'

@app.errorhandler(404)
def not_found(error):
  response = make_response('NOT FOUND', 404)
  return response
