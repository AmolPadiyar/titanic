import pickle
import json
import config
import pandas as pd
import numpy as np


class TitanicPred():

    def __init__(self,PassengerId,Pclass,Gender,Age,SibSp,Parch,Ticket,Fare,Embarked):

        self.PassengerId = PassengerId
        self.Pclass = Pclass
        self.Gender =Gender
        self.Age =Age
        self.SibSp = SibSp
        self.Parch = Parch
        self.Ticket = Ticket
        self.Fare = Fare
        self.Embarked = Embarked

    def load_models(self):

        with open(config.model_path,"rb") as m:
            self.model = pickle.load(m)

        with open(config.json_path,"r") as j :
            self.json_data = json.load(j)

    def get_prediction(self) :

        self.load_models()

        test_array = np.zeros(len(self.json_data["Columns"]),int)

        test_array[0] = self.PassengerId 
        test_array[1] = self.Pclass
        test_array[2] = self.json_data["Gender_Value"][self.Gender]
        test_array[3] = self.Age
        test_array[4] = self.SibSp
        test_array[6] = self.Parch
        test_array[7] = self.Fare

        if self.Ticket in self.json_data["Columns"]:
            ticket_index = self.json_data["Columns"].index("Ticket_"+self.Ticket)
        else:
            self.Ticket = "unique_ticket"
            ticket_index = self.json_data["Columns"].index("Ticket_"+self.Ticket)
            
        test_array[ticket_index] = 1

        embark_index = self.json_data["Columns"].index("Embarked_"+self.Embarked)
        test_array[embark_index] = 1

        print("test array :",test_array)

        if self.PassengerId >=1 and self.PassengerId <=890:
            output = self.model.predict([test_array])

            return output
        else:
            return "This Passanger ID does not belongs to Titanic Pasanger ID list please ensure the Passenger ID"