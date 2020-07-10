import nltk
import re
import random
from nltk.chat.util import Chat, reflections
from yolo_object_detection import ImageCheck

i= ImageCheck()
return_set=i.checkPool()
for s in return_set:
    print(s)

def isThere(obj_name):
    for s in return_set:
        if s == obj_name :      
            return 'YES'
    return 'NO'        
# ans=i.checkPool()
# print(ans)

#overriding Class Chat -> Member function 'respond' 
class MyChat(Chat):

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"  

                # will return YES or NO on the basis of if the object is there      
                return isThere(resp) 


pairs = [
        ['is there a (.*)', ['%1']]
        #  ['is there a pool', [isThere('pool')]],
         
]

chat= MyChat(pairs, reflections)
chat.converse() 