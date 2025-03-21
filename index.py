# 1    
class Star_Cinema:
  hall_list = []
  
  @classmethod
  def entry_hall(cls, hall):
    cls.hall_list.append(hall)
    
class Hall(Star_Cinema):
  def __init__(self, hall_no, rows, cols):
    self.rows = rows
    self.cols = cols
    self.hall_no = hall_no
    self.show_list= []
    self.seats={}
    
    self.entry_hall(self)
    
  def entry_show(self, id, movie_name, time):
    new_show = (id, movie_name, time)
    self.show_list.append(new_show)
    
    seats = []
    for row in range(self.rows):
      row_seats = [0 for i in range(self.cols)]
      seats.append(row_seats)
    
    self.seats[id] = seats
    
  def book_seats(self, id, selected_seats):
    if id not in self.seats:
      print('No show under this id')
      return
    
    seats = self.seats[id]
      
    for seat in selected_seats:
      row, col = seat
        
      if(row < 0 or row >= self.rows or col < 0 or col >= self.cols):
        print(f"Seat [{row}, {col}] is invalid")
        continue
          
      if seats[row][col] == 1:
        print(f"Seat [{row}, {col}] is already booked")
      else:
        seats[row][col] = 1
        print(f"Booking complete for seat [{row}, {col}]")
        
  def view_show_list(self):
    if not self.show_list:
      print("No shows are currently runnig")
      return
        
    for show in self.show_list:
      id, movie, time = show
      print(f"MOVIE NAME: {movie}({id}) SHOW ID: {id} TIME: {time}")
      
  def view_available_seats(self, id):
    if id not in self.seats:
      print("No show found for this id")
      return
    
    print(f"\n\nAvailable seats for show {id}:")
    
    seats = self.seats[id]
    
    for row in range(self.rows):
      for col in range(self.cols):
        if seats[row][col] == 0:
          print(f"Seat [{row}, {col}]")
    
    print(f"\nUpdate seats for Hall {self.hall_no}: ")
    
    for row in self.seats[id]:
      print(row)
            
def cinema_counter():
  hall1 = Hall(hall_no="1", rows = 5, cols= 10)
  
  hall1.entry_show(id="111", movie_name="Jawan Majhi", time="25/10/2023 11:00 AM")
  hall1.entry_show(id="333", movie_name="Sujon Majhi", time="25/10/2023 2:00 PM")
  
  while True:
    print("\n1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    
    choice = input("ENTER OPTION: ")
    
    
    if choice == "1":
      print("------------------")
      hall1.view_show_list()
      print("------------------")
      
    elif choice == "2":
      show_id = input("ENTER SHOW ID: ")
      hall1.view_available_seats(show_id)
      
    elif choice == "3":
      show_id = input("Show Id: ")
      num_seats = int(input("Number of Ticket?: "))
      
      selected_seats = []
      
      for i in range(num_seats):
        row = int(input("Enter Seat Row: "))
        col = int(input("Enter Seat Col: "))
        selected_seats.append((row, col))
        
      hall1.book_seats(id=show_id, selected_seats=selected_seats)
    
    elif choice == "4":
      return
    
    else:
      print("Invalid choice. Please try again.")
      
cinema_counter()