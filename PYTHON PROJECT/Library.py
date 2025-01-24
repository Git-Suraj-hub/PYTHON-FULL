class Library:
    books =["Operating System","MACHINE LEARNING","PYTHON","COMPUTER ORGANIZATION AND ARCHITECTURE",'WEB DESIGNING',"DISCRETE MATHEMATICS"]
    NoOfBooks = len(books)
    def add(self,book):
        self.books.append(book)
        self.NoOfBooks +=1
    def show(self):
        print(f"The Total Books Of Availble in Library : {self.NoOfBooks}")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}) {book}")
        
l1 = Library()
l1.add("O.S.")
l1.show()