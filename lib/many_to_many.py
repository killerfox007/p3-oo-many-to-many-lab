class Author:
    all =[]
    

    def __init__(self, name):
        self._contracts=[]
        self._books=[]
        if isinstance(name, str):
            self.name = name
        else: 
            raise Exception()
    
    def sign_contract(self, book, date, royalties):
       return Contract(self,book,date,royalties)
    def contracts(self):
        return self._contracts
    def books(self):
        return self._books

    def total_royalties(self):
        x = [contract.royalties for contract in self._contracts]
        return sum(x)
class Book:
    all =[]
    def __init__(self, title):
        self._contracts = []
        self._authors = []
        if isinstance(title, str):
            self.title = title
        else: 
            raise Exception()
    def contracts(self):
        return self._contracts
    def authors(self):
        return self._authors

        
        
class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else: 
            raise Exception()
        if isinstance(book, Book):
            self.book = book
        else: 
            raise Exception()
        if isinstance(date, str):
            self.date = date
        else: 
            raise Exception()
        if isinstance(royalties, int):
            self.royalties = royalties
        else: 
            raise Exception()
        author.contracts().append(self)
        author.books().append(book)
        book.contracts().append(self)
        book.authors().append(author)
        Contract.all.append(self)
    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if date == contract.date] 