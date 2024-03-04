class Movie:
    def __init__(self, title, director, genre, release_year):
        self.title = title
        self.director = director
        self.genre = genre
        self.release_year = release_year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Genre: {self.genre}")
        print(f"Release Year: {self.release_year}")

movie1 = Movie(title="Inception", director="Christopher Nolan", genre="Sci-Fi", release_year=2010)
print(f"Movie Title: {movie1.title}")
print(f"Director: {movie1.director}")

movie1.display_info()
