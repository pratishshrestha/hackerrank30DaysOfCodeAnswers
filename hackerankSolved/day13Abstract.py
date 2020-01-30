from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
class Book:

    __metaclass__ = ABCMeta
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author, price)
    
    def display(self):
        print("Title: " + str(self.title))
        print("Author: "+ str(self.author))
        print("Price: "+ str(self.price))

#Write MyBook class

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()