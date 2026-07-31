class Star_Cinema:
    def __init__(self):
        self.__hall_list = []  # Now this is an instance attribute
    
    def entry_hall(self, hall):
        self.__hall_list.append(hall)  # Using instance attribute

    def view_all_halls(self):
        for hall in self.__hall_list:
            print(f"Hall No: {hall.get_hall_no()}, Rows: {hall.get_rows()}, Cols: {hall.get_cols()}")

class Hall:
    def __init__(self, rows, cols, hall_no, cinema):  # Pass an instance of Star_Cinema
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        cinema.entry_hall(self)  # Now calling entry_hall on an instance

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[show_id] = [['Free' for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, show_id, seat_positions):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return
        
        for row, col in seat_positions:
            if not (0 <= row < self.__rows and 0 <= col < self.__cols):
                print(f"Invalid seat position: ({row}, {col})")
                continue
            if self.__seats[show_id][row][col] == 'Booked':
                print(f"Seat ({row}, {col}) is already booked!")
                continue
            self.__seats[show_id][row][col] = 'Booked'
        print("Seats booked successfully!")

    def view_show_list(self):
        for show in self.__show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return

        for row in range(self.__rows):
            print(self.__seats[show_id][row])

    def get_hall_no(self):
        return self.__hall_no

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

# Create an instance of Star_Cinema
cinema = Star_Cinema()

# Now pass that instance to Hall
hall1 = Hall(6, 5, 1, cinema)
hall2 = Hall(8, 4, 2, cinema)

hall1.entry_show("S1", "Movie A", "12:00 PM")
hall1.entry_show("S2", "Movie B", "3:00 PM")

hall1.view_show_list()
hall1.view_available_seats("S1")
hall1.book_seats("S1", [(2, 3), (4, 5), (10, 15)])
hall1.view_available_seats("S1")

cinema.view_all_halls()  # ✅ Now we call it on the instance
