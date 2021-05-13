import spacy
import nltk.data
import requests
import re
import unidecode
from .wiki2 import chatbot
import os

class Main_class():

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


    def main_func(self, content):

        try:
                final_questions = {}
                final_answers = []
                #print(content)
                content = re.sub("\((.*?)\)", "", content)
                content = re.sub("\[(.*?)\]", "", content)
                #print(content)

                for sent in self.tokenizer.tokenize(content):
                    doc = self.nlp(sent)
                    val = self.entity_detection(sent)
                    question = ""
                    ents = self.convert_entity_to_text(doc.ents)
                    answer = self.convert_to_mcq(ents, sent)
                    if answer is None:
                        answer = self.convert_to_mcq(val,sent)
                    if answer is not None:
                        final_questions[answer[0]] = answer[1]
                return final_questions
        except:
            return "<h1> Oops!!! Something went wrong. Please try again in some time.</h1>"

    def write_to_file(self, question, answers):

        with open("main/assets/MCQ.txt", "a") as file:
            file.write("\n"*2)
            file.write("Question : " + question + "\n")
            #print("Question : " + question)

            for answer in answers:
                #print(answer)
                file.write(" "*4+"• " + answer + "\n")

    def convert_to_mcq(self, val, sent):
        #   print(sent)
        val = set(val)
        if len(val) <=4:
            for noun in set(val):
                #print(noun)
                c = chatbot(noun)
                try:
                    related_names = c.get_related_names()
                    #print(" #########  ", related_names)
                    if related_names is not None:
                        related_names = set(related_names[:3])
                        #print(" related_names : ", related_names, related_names!= {})
                        if related_names != {}:

                            question  = sent.replace(noun,"_ "*(len(noun)), 1)

                            if len(set(related_names).intersection(val))<=1:
                                return_val = related_names.difference(val)
                                return_val = return_val.union(set([noun+" (correct answer) "]))
                                if len(return_val) >= 4:
                                    return_val = list(return_val)

                                    self.write_to_file(question, return_val)
                                    #print(question, return_val)

                                    for i in range(len(return_val)):
                                        val = return_val[i]
                                        val = "<li> "+ val + "</li>"
                                        return_val[i] = val
                                    return question, ''.join(return_val)
                except:
                    pass

    def entity_detection(self, statement):
        doc = self.nlp(statement)
        pos_list = []
        temp = []
        for i in range(len(doc)):
            curr_pos = doc[i].pos_
            word = doc[i]
            #print(word, " : ",curr_pos)
            pos_list.append(curr_pos)
            if curr_pos == "PROPN":
                if i != 0 :
                    if ( doc[i-1].pos_ == "ADP"  or doc[i-1].pos_ == "PROPN"):
                        if temp != []:
                            if doc[i-1].pos_ == "ADP":
                                temp[-1] += " " + str(doc[i-1].text) + " " + str(word.text)
                            else:
                                temp[-1] += " "  + str(word.text)
                        else:
                            temp.append(str(word.text))
                    else:
                        temp.append(str(word.text))
                else:
                    temp.append(word.text)
        if temp == []:
            return []
        else:
            return temp

    def convert_entity_to_text(self, entities):
        names = []
        for entity in entities:
            names.append(entity.text)
        return names
