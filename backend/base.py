from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import INT

api = Flask(__name__)
app.config['postgresql://neeladri:AoT-QZ3YfWYfEuPMIMLrKg@cloudy-cyclops-6954.5xj.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full'] = 'cockroachdb://neeladri:AoT-QZ3YfWYfEuPMIMLrKg@host:port/defaultdb'
db = SQLAlchemy(app)
# test


@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Aarushi",
        "about": "i like feet"
    }
    return response_body


@api.route('/sign_up')
def signUp():
    response_body = {
    }

    return response_body


@api.route('/feed')
def my_feed():
    response_body = {
    }

    return response_body
