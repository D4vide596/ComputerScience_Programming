class BookRentalAccount:
    def __init__(self, name, points, rentals, books):
        self.name = name
        self.points = points
        self.rentals = rentals
        self.books = books

    def rent_book(self, book):
        if self.points > book['points']:
            self.points -= book['points']
            self.rentals.append(book)
            print(f"you rented {book}")
        else:
            print(f"not enough points to rent the book {book}")

    def print_user_details(self):
        print(f"Name: {self.name}\n"
              f"Points: {self.points}")
        if len(self.rentals) > 0:
            print(f"Books rented:")
            counter=1
            for book in self.rentals:
                print(f"#{counter}", end="")
                for key, value in book.items():
                    print(f" - {key}: {value}", end="")
                print()
                counter+=1
        else:
            print("no books rented yet! Take something to read..")


if __name__ == '__main__':

    books = [
        {"title": "Treasure Island", "author": "Robert Louis Stevenson", "points":1, "pages": 292},
        {"title": "Mobi Dick", "author": "Herman Melville", "points":2, "pages": 378},
        {"title": "Around the World in 80 Days", "author": "Jules Verne", "points":1, "pages": 149},
        {"title": "Gulliver's Travels", "author": "Jonathan Swift", "points": 3, "pages": 352},
        {"title": "Frankenstein", "author": "Mary Shelly", "points": 2, "pages": 280},
        {"title": "The Call of Cthulhu and Other Weird Stories", "author": "H.P. Lovecraft", "points": 3, "pages": 420},
    ]

    book_rental_account = BookRentalAccount(name='Marty McFly', points=5, rentals=[], books=books)
    book_rental_account.print_user_details()
    book_rental_account.rent_book(books[1])
    book_rental_account.rent_book(books[2])
    book_rental_account.rent_book(books[5])
    book_rental_account.print_user_details()
