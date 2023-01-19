class publisher:
   def __init__(self,pubname):
       self.pubname=pubname
   def display(self):
       print("publisher name:",self.pubname)
class book(publisher):
    def __init__(self,pubname,title,author):
        publisher.__init__(self,pubname)
        self.title=title
        self.author=author
    def display(self):
        print("title:",self.title)
        print(("author:",self.author))
class python(book):
    def __init__(self,pubname,title,author,price,no_of_pages):
        book.__init__(self,pubname,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        print("title:",self.title)
        print("author:",self.author)
        print("publisher:",self.pubname)
        print("price:",self.price)
        print("no of pages:",self.no_of_pages)
b1=python("New india","python for babies","mark liyo",650,900)
b1.display()


