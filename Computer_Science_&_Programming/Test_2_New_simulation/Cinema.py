class CinemaHall:
    def __init__(self, movie_name, room_number, total_seats):
        self.movie_name = movie_name
        self.room_number = room_number
        self.total_seats = total_seats
        self.tickets_sold = 0

    def sell_ticket(self):
        if self.tickets_sold < self.total_seats:
            self.tickets_sold += 1
        else:
            print("Sold out!")

    def print_info(self):
        print(f"Movie: {self.movie_name} | Room: {self.room_number} | Sold: {self.tickets_sold}/{self.total_seats}")


if __name__ == '__main__':
    # Creates a hall for the movie "Avatar", inside Room 1, with 5 seats total
    h1 = CinemaHall(movie_name="Avatar", room_number=1, total_seats=5)

    h1.print_info()
    h1.sell_ticket()
    h1.sell_ticket()
    h1.sell_ticket()
    h1.print_info()
    # At this point, 3 tickets are sold, 2 are free.

except A
