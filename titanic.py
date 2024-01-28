from flask import Flask,request,render_template
from model import Model

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":

        Pclass = request.form["pClass"]
        Pclass = int(Pclass)

        Sex = request.form["Gender"]
        Sex = int(Sex)

        Age = request.form["Age"]
        Age = int(Age)

        SibSp = request.form["SibSp"]
        SibSp = int(SibSp)

        Parch = request.form["Parch"]
        Parch = int(Parch)

        Fare = request.form["Fare"]
        Fare = float(Fare)

        Embarked = request.form["Embarked"]
        embark = {"S":0,"C":1,"Q":2}
        Embarked = embark[Embarked]
            
        print("Form Values: ",Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)

        model = Model()
        prediction = model.get_prediction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)

        print("prediction: ",prediction)

        return render_template("Test.html",result=prediction,prediction=True)
    else:
        return render_template("Test.html",prediction=False)

if __name__ == '__main__':
    app.run(debug=True)
