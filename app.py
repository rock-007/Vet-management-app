from flask import Flask, render_template, request, redirect
import repositories.admin_repository as admin_repository
import pdb

from controllers.login import login_blueprint
from controllers.customers import customer_blueprint
from controllers.appointments import appointment_blueprint
from controllers.pets import pet_blueprint


app = Flask(__name__)

app.register_blueprint(login_blueprint)
app.register_blueprint(customer_blueprint)
app.register_blueprint(appointment_blueprint)
app.register_blueprint(pet_blueprint)


@app.route("/", methods=["GET", "POST"])
def main():
    email = None
    admin_status = admin_repository.get_status()
    if(request.method =='GET' and type(admin_status) != str ):
        return redirect("/login")
    elif(request.method =='GET' and type(admin_status) == str):
        email = admin_status
        return render_template('index.html', email= email)
    else:
        email = request.form['email_id']
        admin_repository.set_status(email)
        return render_template('index.html', email= email)

if __name__ == "__main__":
    app.run()