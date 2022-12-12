from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db


auth = Blueprint('auth',__name__)


@auth.route('/data')
def data():
    return render_template("data.html", boolean=True)

@auth.route('/information')
def information():
    return render_template("information.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

