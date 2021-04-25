from flask import Flask, Blueprint, redirect, render_template, request


login_blueprint = Blueprint("login", __name__)


#login_page
@login_blueprint.route("/login", methods=["GET","POST"])
def login():
    
    return render_template("login_page/index.html")


