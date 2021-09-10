# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
import requests
import pandas as pd
import numpy 

class ActionCheckWeather(Action):

    def name(self)-> Text:
        return "action_get_weather"
    
    def run(self, dispatcher, tracker, domain):
        #api_key = 'Your API Key'
        loc = tracker.get_slot('location')
        #current = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(loc, api_key)).json()
        #print(current)
        #country = current['sys']['country']
        #city = current['name']
        #condition = current['weather'][0]['main'    ]
        #temperature_c = current['main']['temp']
        #humidity = current['main']['humidity']
        #wind_mph = current['wind']['speed']
        #response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
        #dispatcher.utter_message(response)
        #return [SlotSet('location', loc)]
        df=pd.read_csv(r'./file.csv')
        a=df[df["City"]==loc]
        condition=a["Condition"].values
        condition=numpy.array(condition)
        condition=str(condition).lstrip('[').rstrip(']')

        temperature=a["Temperature"].to_numpy()
        temperature=numpy.array(temperature)
        temperature=str(temperature).lstrip('[').rstrip(']')

        humidity=a["Humidity"].to_numpy()
        humidity=numpy.array(humidity)
        humidity=str(humidity).lstrip('[').rstrip(']')

        wind=a["Wind"].to_numpy()
        wind=numpy.array(wind)
        wind=str(wind).lstrip('[').rstrip(']')

        city=a["City"].to_numpy()
        city=numpy.array(city)
        city=str(city).lstrip('[').rstrip(']')
        #print("Temperature dispatcher:",temperature)
        #response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, loc, temperature, humidity, wind)
        response = """It is currently {} in {} at the moment.\n The temperature is {} degrees.\n The humidity is {} and the wind speed is {} mph.""".format(condition, city, temperature, humidity, wind)
        dispatcher.utter_message(response)
        return [SlotSet('location', city)]


class ActionCheckTeamInfo(Action):

    def name(self)-> Text:
        return "action_get_team"
    
    def run(self, dispatcher, tracker, domain):
        #api_key = 'Your API Key'
        id = tracker.get_slot('Id')
        #print("id is",id)
        df=pd.read_csv(r'./hr.csv')
        print(df["EmpID"].head(2))
        a=df[df["EmpID"]==int(id)]
        #print("a is",a)
        condition=a["Employee_Name"].values
        condition=numpy.array(condition)
        condition=str(condition).lstrip('[').rstrip(']')
        #print(condition)

        position=a["Position"].values 
        position=numpy.array(position)
        position=str(position).lstrip('[').rstrip(']')

        response="""The name of the employee is {}, and department is {}""".format(condition,position)
        dispatcher.utter_message(response)
        return [SlotSet('Id', id)]

class ValidateReimbursementForm(FormValidationAction):

    def name(self)->Text:
        return "validate_reimbursement_form"

    @staticmethod
    def is_int(string: Text)->bool:

        try:
            int(string)
            return True  
        except ValueError:
            return False

    def validate_people(
        self,
        value:Text,
        dispatcher:CollectingDispatcher,
        tracker:Tracker,
        domain: Dict[Text,any]
        )-> Dict[Text,any]:  

        if self.is_int(value) and int(value)>0:
            return {"people":value}
        else:
            dispatcher.utter_message(response="utter_wrong_num_people")

    def validate_days(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text,any]
        )-> Dict[Text,any]:  

        if self.is_int(value) and int(value)>0:
            return {"days":value}
        else:
            dispatcher.utter_message(response="utter_wrong_num_days")
        
    def validate_charge(
        self,
        value: float,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text,any]
        )-> Dict[Text,any]:  

        if self.is_int(value) and int(value)>0:
            return {"charge":value}
        else:
            dispatcher.utter_message(response="utter_wrong_charge")
        
