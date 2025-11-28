#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__ (self, first_name , last_name):
        super().__init__(first_name , last_name)
        self.knowledge = []
    
    def learn(self , knowledge):
        if isinstance(knowledge , str):
            self.knowledge.append(knowledge)
        else:
            raise ValueError('the knowledge passed is not a string')
    
