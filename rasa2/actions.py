# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionCheckSearch(Action):

    def name(self) -> Text:
        return "action_check_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response= requests.get("http://127.0.0.1:8000/image/get_all_objects/").json()

        prediction = tracker.latest_message

        slot_val= tracker.get_slot(prediction['entities'][0]["entity"])
        entity_val = prediction['text'][prediction['entities'][0]['start']:prediction['entities'][0]['end']]

        # print(slot_val)
        # print(prediction['entities'][0]['start'])
        # print(prediction['entities'][0]['end'])
        # print("yo")
        # print( entity_val)
        # print("yo")

        isThere = False
        for r in response:
            #print(r['object_name'])
            if r['object_name'] == slot_val:
                isThere = True

        if isThere:
            dispatcher.utter_message(text="Yes, {} is available".format(entity_val))
        else:
            dispatcher.utter_message(text="Sorry, {} isn't available".format(entity_val))

        return []

    # def name(self) -> Text:
    #     return "action_hello_world"

    # def run(self, dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    #     dispatcher.utter_message(text="Hello World!")

    #     return []
