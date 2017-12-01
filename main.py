
from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

templates_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(templates_dir), autoescape =True)


def verifyUserName(userName):
    if len(userName)<3:
        return False
    elif len(userName)>20:
        return False
    else:
        return True
      
def verifyPassword(password, password2):
    count = 0
#Rule 1
    for item in password:
        if item == " ":
            return False
            break
        else:
            for item in password2:
                if item == " ":
                    return False
                    break
    # Rule 2
    for p in password:
        pas = [password, password2]
    for p in pas:
        if len(p)<3:
            return False
            break
        elif len(p)>20:
            return False
            break
        else: pass
    if password==password2:
        return True
    else:
        return False

def verifyEmail(email):
    if len(email) == 0:
        return True
    countAt = 0
    countDot = 0
    # rule 1
    if len(email)<3:
        return False
    elif len(email) > 20 :
        return False
    else:
        for item in email:
            if item == "@" :
                countAt += 1
            elif item == ".":
                countDot += 1
            elif item ==" ":
                return False
            else:
                continue
        if countAt != 1:
            return False
        elif countDot != 1:
            return False
        else:
            return True 
         
app = Flask(__name__)
app.config["DEBUG"] = True



@app.route("/")
def index():
    return render_template("form.html")





@app.route("/validate_form", methods=["POST"])
def validateInfo():
    nameError = ""
    passwordError = ""
    emailError = ""

    usrName = request.form["username"]
    password = request.form["password"]
    secondPassword = request.form["password2"]
    email = request.form["email"]

    if verifyUserName(usrName) == False:
       nameError = "This is invalid"
    elif  verifyPassword(password, secondPassword) == False:
        passwordError = "This is invalid"
    elif verifyEmail(email) == False:
         emailError= "This is invalid"

    if nameError or passwordError or emailError:
        return render_template("form.html", name_error = nameError, password_error = passwordError, email_error = emailError)
    else:
        return hello()





@app.route("/greetings", methods=["POST"])
def hello():
    usrName = request.form["username"]
    return render_template("greetings.html", name = usrName)

app.run()