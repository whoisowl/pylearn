class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({
            "title": title,
            "author": author
        })

    def remove_book(self, title):
        for index, book in enumerate(self.books):
            if book["title"] == title:
                self.books.pop(index)
                break

    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return book
            

        print("Sorry, this book doesn't exist!")

    def show_books(self):
        return self.books


