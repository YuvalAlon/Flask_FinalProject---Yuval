"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FinalProject import app
from FinalProject.models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines




from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError




from FinalProject.models.QueryFormStructure import UserRegistrationFormStructure 

from FinalProject.models.Forms import ExpandForm
from FinalProject.models.Forms import CollapseForm

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

db_Functions = create_LocalDatabaseServiceRoutines()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        img_nbalogo = '/static/img/nbalogo.png'
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        img_imageskies = '/static/img/imageskies.jpg',
        img_tichonet = '/static/img/tichonet.png'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
                'about.html',
        year=datetime.now().year,
        img_tichonet = '/static/img/tichonet.png'
    )

@app.route('/data/assignment5130' , methods = ['GET' , 'POST'])
def assignment5130():

    print("5130")

    return render_template(
        'assignment5130.html'
    )


@app.route('/data/regularstats' , methods = ['GET' , 'POST'])
def regularstats():

    print("regularstats")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    # df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\regular.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/regular.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'regularstats.html',
        title='regularstats',
        year=datetime.now().year,
        message='regular stats dataset page.',
        img_lebronjames = '/static/img/lebronjames.jpg',
        img_kobebeans = '/static/img/kobebeans.jpg',
        img_zionwilliamson = '/static/img/zionwilliamson.jpg',
        img_michaeljordan = '/static/img/michaeljordan.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )

@app.route('/data/per36' , methods = ['GET' , 'POST'])
def per36():

    print("per36")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\per36.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'per36.html',
        title='per36',
        year=datetime.now().year,
        message='per36 dataset page',
        img_lebronjames = '/static/img/lebronjames.jpg',
        img_kobebeans = '/static/img/kobebeans.jpg',
        img_zionwilliamson = '/static/img/zionwilliamson.jpg',
        img_michaeljordan = '/static/img/michaeljordan.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )

@app.route('/data')
def data():

    print("Data")

    """Renders the about page."""
    return render_template(
        'data.html',
        title='Data',
        year=datetime.now().year,
        message='My data page.',
        img_zionwilliamson = '/static/img/zionwilliamson.jpg',
        img_kobebeans = '/static/img/kobebeans.jpg',
        img_michaeljordan = '/static/img/michaeljordan.jpg',
        img_lebronjames = '/static/img/lebronjames.jpg'
    )

@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thank You, You Will Register Now :) '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='In This Page You Can Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )