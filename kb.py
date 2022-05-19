# see Program 4 in https://gvanrossum.github.io/docs/PyPatternMatching.pdf
# for an example (hack) of dynamic function overloading
from q import easy_input
from collections import ChainMap,defaultdict
from unittest import TestCase
from random import randint
import pdb

class knowledge(object):
    """ george is a good little monkey, but always curious"""

    gibberish = 'Hoo! Hoo! Ha! Ha!'
    mlue = "the meaning of Life, the Universe, and Everything"
    the_ultimate_question = "the Ultimate Question"
    defaults = {the_ultimate_question: None}
    the_ultimate_answer = 42
    uq = defaultdict(lambda: knowledge.ua)

    who = {"Who is Mommy": "Mother"}
    what = {"What is the Man in the Yellow Hat": "Man"
           ,"What is Person": "kindof Animal"
           ,"What is Animal": "kindof Living Thing"
           ,"What is Man": "kindof Person"
           ,"What is Man": "Male Person"
           ,"What is Hat": "kindof Covering"
           ,"What is Hat": "Covering for Head"
           ,"What Hat is madeof": "Straw"
           ,"What is Straw": "partof kindof Plant"
           ,"What is Plant": "kindof Living Thing"
           ,"What is Head": "partof Person"
           ,"What is Yellow": "kindof Color"
           ,"What is Color": "propertyof Thing"
           ,"What Color is Straw": "Yellow"
           ,"What is Woman": "kindof Person"
           ,"What is Woman": "Female Person"
           ,"What is Child": "kindof Person"
           ,"What is Child": "Young Person"
           ,"What is Baby": "New Person"
           ,"What is Fetus": "Baby in Mother"
           ,"What is Mother": "Woman having Baby"
           }
    where = {"Where is Mommy": "School"
            ,"Are we there, yet": "No"
            ,"Are we there, yet": "Almost" # where answers can change 
            }
    when = {"When will Mommy be Home": "Dinner Time"
           ,"When is Dinner Time": "6:30 PM"
           ,"Is it Dinner Time, yet": "No"
           ,"Is it Dinner Time, yet": "No"
           ,"Is it Dinner Time, yet": "Almost" # when answers can change 
           }
    why = {"Why": "Because"} # why answers can probably change, too

    def __init__(self):
        """ mock knowledge base, use triple store ? """ 
        self.base = ChainMap(self.who
                            ,self.what
                            ,self.where
                            ,self.when
                            ,self.why
                            ,self.defaults
                            ,self.uq
                            )

    def __iter__(self):
        return(self)

    def __next__(self):
        return self.next()

    def next(self):
        while True:
            try:
                for q in self.base.keys():
                    if not(self.the_ultimate_answer == self.base[q]):
                        yield q
            finally:
                raise StopIterator
        # print("base = {}".format(self.base))

    def close(self):
        # persist knowledge base
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc, value, tb):
        self.close()

    def ask(self,question):
        #return input("{} ".format(question))
        if self.gibberish == question:
            return None
        response = self.base[question.rstrip('?')]
        if response and self.the_ultimate_answer != response:
            return response
        # return easy_input(question+"?",[False,True])
        response = randint(0,2)
        # finite improbability drive
        if response < 2:
            if bool(response):
                return 'Yes'
            else:
                return 'No'
        else:
            return 'Dunno'

    def answer(self,question):
        response = None
        print('Q: {}'.format(question))
        k = question.rstrip('?')
        response = self.ask(question)
        print('A: {}'.format(str(response)))
        return response

def test(the,q,a):
     #pdb.set_trace()
     response = the.answer(q)
     if knowledge.the_ultimate_question == q or 'Dunno' == response:
         pass
     else:
         TestCase().assertEquals(response,a)

if __name__ == '__main__':
     """
     with knowledge() as qa:
         (qa.answer(question) for question in qa)
     """
     oracle=knowledge()
     test(oracle,'Where is Mommy?','School')
     test(oracle,'Are we there, yet?','Almost')
     test(oracle,knowledge.gibberish,None)
     test(oracle,knowledge.the_ultimate_question,'Dunno')
