# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckSearch(Action):

    def name(self) -> Text:
        return "action_check_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        check= tracker.get_slot("check")
        isThere= "Yes"
        dispatcher.utter_message(text="{}, {} is available".format(isThere, check))

        return []

    # def name(self) -> Text:
    #     return "action_hello_world"

    # def run(self, dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    #     dispatcher.utter_message(text="Hello World!")

    #     return []
