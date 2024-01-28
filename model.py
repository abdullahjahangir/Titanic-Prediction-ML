import pickle
class Model:
    def get_prediction(self,Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
        l = [[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]]
        print("L: ",l)
        with open("static/model/logistic_model_titanic_prediction.pickle","rb") as f:
            rmodel = pickle.load(f)
        X_train_prediction = rmodel.predict(l)[0]
        if X_train_prediction == 0:
            return False
        else:
            return True
