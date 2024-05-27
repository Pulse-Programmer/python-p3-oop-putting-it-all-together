#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size) -> None:
        self.brand = brand
        self.size = size
        
        
    @property
    def size(self):
        print("size getter called")
       
        return self._size
        
    @size.setter
    def size(self, value):
        if type(value) in (int,):
            self._size = value
        else:
            print("size must be an integer")
            
            
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"