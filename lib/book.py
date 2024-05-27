#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count) -> None:
        self.title = title
        self.page_count = page_count
    
        
    @property
    def page_count(self):
        print("page_count getter called")
       
        return self._page_count
        
    @page_count.setter
    def page_count(self, value):
        if type(value) in (int,):
            self._page_count = value
        else:
            print("page_count must be an integer")
            
            
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")