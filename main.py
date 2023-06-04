from flask import Flask , render_template,request
from project_file.utils import TitanicPred


app = Flask(__name__)

@app.route("/")
def home_api():
    print("we are in home api")
    return render_template("index.html")

@app.route("/get_pred",methods = ["GET","POST"])
def get_prediction():
    if request.method == "GET":

        PassengerId = eval(request.args.get("PassengerId")) 
        Pclass = eval(request.args.get("Pclass"))
        Gender = request.args.get("Gender")
        Age = eval(request.args.get("Age"))
        SibSp = eval(request.args.get("SibSp"))
        Parch = eval(request.args.get("Parch"))
        Ticket = request.args.get("Ticket")
        Fare = eval(request.args.get("Fare"))
        Embarked = request.args.get("Embarked")

        obj = TitanicPred(PassengerId,Pclass,Gender,Age,SibSp,Parch,Ticket,Fare,Embarked)
        
        predction = obj.get_prediction()

        one = "The Person is Survived"
        zero = "The Peson is Not Survived"
        error = "This Passanger ID does not belongs to Titanic Pasanger ID list please ensure the Passenger ID"
        if predction == 1:
            return render_template("index.html",result=one)
        elif predction == 0 :
            return render_template("index.html",result=zero)
        else:
            return render_template("index.html",result=error)
        
if __name__ == "__main__":
    app.run()