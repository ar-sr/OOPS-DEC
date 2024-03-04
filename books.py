class book:
    def __init__(self,title,author,genre,publication_year):
        self.title=title
        self.author=author
        self.genre=genre
        self.publication_year=publication_year
        
        
    def display_info(self):
        print(f"title:{self.title}")
        print(f"author:{self.author}")
        print(f"genre:{self.genre}")
        print(f"publication_year:{self.publication_year}")
        
        
        
    # def book1(self):
        
    #     book_title=input("enter the name of books:")
    #     book_author=input("enter the name of the author:")
    #     book_genre=input("enter the genre of the book:")
    #     book_year=int(input("enter the year of publication:"))
            
            
            
my_book=book(
    title=input("enter the name of books:"),
    author=input("enter the name of author:"),
    genre=input("enter the genre of book:"),
    publication_year=input("enter the year of publication:"))


my_book.display_info()
print(my_book)
                    
        

        
        
        
        
        
           
    