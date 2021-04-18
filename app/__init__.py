from flask import Flask # creates the application object as an instance of class Flask imported from the flask package
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app= Flask(__name__)    # the __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used
app.config.from_object(Config)
db=SQLAlchemy(app)      # create database instance
migrate= Migrate(app, db)# database migration engine instance
from app import routes, models  # importing the routes module and models module that will define the database structure
                        # The bottom import is a workaround to circular imports, a common problem with Flask applications
