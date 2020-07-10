import nltk
import re
import random
from nltk.chat.util import Chat, reflections
from yolo_object_detection import ImageCheck

i= ImageCheck()
objects=i.checkPool()
for s in objects:
    print(s)

# objects= set()
# objects.add("car")
# objects.add("pool")
# objects.add("bed")
# for s in objects:
#     print(s)

# overriding Class Chat -> Member function 'respond'
class MyChat(Chat):

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """
        # riya's code for sentence noun detection
        sentences = nltk.sent_tokenize(str)
        nouns = []
        # code for extracting nouns
        for sentence in sentences:
            for word, pos in nltk.pos_tag(nltk.word_tokenize(sentence)):
                if(pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                    nouns.append(word)
        response = "No"
        #returns yes if there is a match
        for noun in nouns:
            if noun in objects: 
                response = "Yes"

        return response

        # check each pattern
        
        # for (pattern, response) in self._pairs:
        #     match = pattern.match(str)

        #     # did the pattern match?
        #     if match:
        #         resp = random.choice(response)  # pick a random response
        #         resp = self._wildcards(resp, match)  # process wildcards

        #         # fix munged punctuation at the end
        #         if resp[-2:] == "?.":
        #             resp = resp[:-2] + "."
        #         if resp[-2:] == "??":
        #             resp = resp[:-2] + "?"

        #         # will return YES or NO on the basis of if the object is there
        #         return resp



pairs = [
        ['(.*)', ['%1']]
    #  ['is there a pool', [isThere('pool')]],

]

chat = MyChat(pairs, reflections)
chat.converse()
