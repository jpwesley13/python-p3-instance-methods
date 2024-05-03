#!/usr/bin/env python3

class Dog:
    def bark(self): 
        # "self" is required for instance method definitions, but does not need to be passed when calling the method.
        print("Woof!")
    
    def sit(self):
        print("The dog is sitting.")