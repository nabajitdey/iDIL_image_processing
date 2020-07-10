import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk import word_tokenize,sent_tokenize,pos_tag
from yolo_object_detection import ImageCheck

#getting the set of objects detected
i= ImageCheck()
objects=i.checkPool()
for s in objects:
    print(s)

isContinue='y'

while isContinue == 'y':
    query = input("question: ") 
    sentences = nltk.sent_tokenize(query)
    nouns = []
    #code for extracting nouns
    for sentence in sentences:
        for word,pos in nltk.pos_tag(nltk.word_tokenize(sentence)):
            if(pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                nouns.append(word)
    #print(nouns)
    #returns labels of the detected objects

    response = "No"
    #returns yes if there is a match
    for noun in nouns:
        if noun in objects: 
            response = "Yes"
    print(response)
    isContinue=input("continue? ")
