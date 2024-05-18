"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


user = 'root'
password = 'Yazm1n25'
host = 'localhost'
name = 'cafeteria'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}/{name}'
db = SQLAlchemy(app)

import Cafe.views
