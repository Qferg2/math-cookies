import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #SECRET_KEY is an environment variable.  
                                         #The value should be set in Heroku (Settings->Config Vars).  

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    #TODO: delete everything from the session
    session.clear()
    return redirect('/')

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    #TODO: save the first and last name in the session
    #session["last_name"] = request.form["lastName"]
    session["sum"] = request.form["sum"]
    return render_template('page2.html')
  
@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    #TODO: save the first and last name in the session
    #session["last_name"] = request.form["lastName"]
    return render_template('page3.html')
  
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    #TODO: save the first and last name in the session
    #session["last_name"] = request.form["lastName"]
    return render_template('page4.html')

@app.route('/page5',methods=['GET','POST'])
def renderPage5():
    #TODO: save the favorite color in the session
    #session["favorite_color"] = request.form["favoriteColor"]

    if session[sum] == 15:
        response = "YAY"
    else:
        response = "OOPS"

    if session["sum"] == 15:
        AdAnswer = "YAY"
    else:
        AdAnswer = "OOPS"

    return render_template('page5.html')
    
if __name__=="__main__":
    app.run(debug=True)
