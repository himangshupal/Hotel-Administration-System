'''
Project: Hotel Room Management Application
Author: Himangshu Pal
Version: 1.0
Date Created: May 18, 2019
Description:
Hotel Room Management Application is an online system to perform room booking and
cancellation activity.

Two classes are defined for this purpose.

Room Class: to perform activities on room objects.
Hotel Class: reservation, cancellation, daily accounting and room setup activities.

Special Instruction: If you are using Pycharm then right click
and run 'Hotel' to execute the application.
'''

class Room:

    def __init__(self, roomNum, bedType, smoking, rate):

        self.roomNum = roomNum
        self.bedType = bedType
        self.rate = rate
        self.smoking = smoking
        self.occupantName = "Not occupied"
        self.occupied = False

# Instance variables:
# roomNum: Room Number, Integer
# bedType: String, 'Twin', 'King' and 'Queen'
# rate: Float.
# smoking: String, 'n' and 's'
# occupantName: String, default value 'Not Occupied'
# occupied: Boolean, default False

# Getter method section.

# getBedType : string type. Returns Bed types 'Queen', 'King' and 'Twin'.
    def getBedType(self):
        return self.bedType

# getSmoking: boolean type. If smoking is allowed in the room. Return 'n' - No smoking, 's' - Smoking
    def getSmoking(self):
        return self.smoking

# getRoomNum: Integer type. Return room number.
    def getRoomNum(self):
        return self.roomNum

# getOcccupant: String type. Returns the name of the occupant if room is occupied.
    # Else returns 'Not Occupied'.
    def getOccupant(self):
        return self.occupantName

# getRoomRate: Float. Returns price per night.
    def getRoomRate(self):
        return self.rate

# getOccupyflag: Boolean. Returns True is occupied else False.
    def setOccupied(self, occupyflag):
        self.occupied = occupyflag

# Setter method section.

# setOccupant: String. Update the name of the occupant in Room type object.
    def setOccupant(self, name):
        self.occupantName = name

# setRoomNum: Integer. Update the room number in room type object.
    def setRoomNum(self, number):
        self.roomNum = number

# setBedType: String. Update the type of bed in a rooms, 'Queen', 'King', 'Twin'.
    def setBedType(self, bedtype):
        self.bedType = bedtype

# setRate: Float. update per night price of a room.
    def setRate(self, price):
        self.rate = price

# setSmoking: String. Set flag value 'n' for Non-smoking and 's' for Smoking room.
    def setSmoking(self, smoking_flag):
        self.smoking = smoking_flag

# isOccupied: Boolean. Checks if room is occupied. Return 'True' if occupied else returns 'False'.
    def isOccupied(self):
        return self.occupied

# Returns Room No, Bed Type, Smoking, Price, Room Status (Occupied and Occupant name).
    def __str__(self):

        return f"Room Number: {self.roomNum}\n" \
            f"Occupant Name: {self.occupantName}\n" \
            f"Smoking Room: {self.smoking}\n" \
            f"Bed Type: {self.bedType}\n" \
            f"Rate: {self.rate}\n\n"

# End of Room Class


class Hotel:

    def __init__(self, name, location):

        self.name = name
        self.location = location
        self.theRooms = []
        self.occupiedCnt = 0
        self.numOfRooms = 0

    # Instance variables:
    # name: String, name of hotel
    # location: String, location of hotel
    # theRooms: Array to hold room type objects.
    # occupiedCnt: Integer, count of occupied rooms.
    # numOfRooms: Integer, number of rooms in the hotel, increments when room type objects get created.

# isFull method: If hotel is full then occupiedCnt equals numOfRooms.Returns boolean values.
    def isFull(self):
        return self.occupiedCnt == self.numOfRooms

# isEmpty method: If hotel is empty,occupiedCnt is 0, returns True else False.
    def isEmpty(self):
        return self.occupiedCnt == 0


# addRoom: input parameters room number, bedtype, smoking flag, price.
    # append room type objects into theRoom array. The array can hold maximum 10 rooms.
    def addRoom(self, roomnumber, bedtype, smoking, price):

        if self.numOfRooms == 10:
            return "No more rooms to create."

        self.theRooms.append(Room(roomnumber, bedtype, smoking, price))
        self.numOfRooms += 1
        return "{roomnumber} is created."

# __printAllRooms: private method to arrange Room Details.
    def __printAllRooms(self):
        temp_room = ""
        for i in range(self.numOfRooms):
            temp_room+= self.theRooms[i].__str__()
        return temp_room

# Print Hotel and Room details.
    def __str__(self):

        room_detail = self.__printAllRooms()
        temp = f"Hotel Name: {self.location} {self.name} \n" \
            f"Number of rooms: {self.numOfRooms}\n" \
            f"Number of Occupied Rooms: {self.occupiedCnt}\n\n\n" \
            f"Room details are: " \
            f"\n\n{room_detail}"
        return temp

# addReservation:
    #input: occupant name, smoking flag, bed type.

    def addReservation(self, occupantName, smoking, bedType):
        isBooked = False
        if self.isFull():
            print("No vacancy!!!")
            return
        else:
            for room in self.theRooms:
                if room.isOccupied() == False:
                    if ((bedType == room.getBedType()) and (smoking == room.getSmoking())):
                        room.setOccupied(True)
                        room.setOccupant(occupantName)
                        print(f"{room.getRoomNum()} is booked for {room.getOccupant()}.")
                        isBooked = True
                        self.occupiedCnt+=1

            if not isBooked:
                print(f"Sorry no room available for {bedType}, {smoking}.")

# __findReservation: Private method to find if there is any reservation for a given occupant
    # name. Input: Occupant name. Output: list of objet index for all bookings found
    # or -1 for no booking found.
    def __findReservation(self, occupantName):

        not_found = -1
        index = 0
        temp = []
        for room in self.theRooms:
            if occupantName == room.getOccupant():
                not_found = 0
                temp.append(index)
            index+=1

        if not_found == -1:
            return not_found
        else:
            return temp


# cancelReservation: cancels the reservation of the input occupant name.
    # Input- occupant name.
    def cancelReservation(self, occupantName):

        room_index = self.__findReservation(occupantName)

        if room_index == -1:
            print(f"No reservation found to cancel for {occupantName}")
        else:
            for i in room_index:
                self.theRooms[i].setOccupied(False)
                self.theRooms[i].setOccupant('Not occupied')
                print(f"Room number {self.theRooms[i].getRoomNum()} for {occupantName} is cancelled.")
                self.occupiedCnt-=1

# printReservationList: print all reserved rooms details
    def printReservationList(self):

        if self.isEmpty():
            print("No reservation found.")
            return

        for room in self.theRooms:
            if room.isOccupied():
                print(f"####  Reservation List ####\n"
                    f"Room Number: {room.getRoomNum()}\n"
                      f"Occupant name: {room.getOccupant()}\n"
                    f"Smoking room: {room.getSmoking()}\n"
                    f"Bed type: {room.getBedType()}\n"
                    f"Rate: {room.getRoomRate()}\n")


# getDailySales: calculate total sale amount for a day.
    def getDailySales(self):

        daily_sale_amount = 0

        if self.isEmpty():
            print(f"Daily sale amount is {daily_sale_amount}")
        else:
            for room in self.theRooms:
                if room.isOccupied():
                    daily_sale_amount+=room.getRoomRate()
            print(f"Daily sale amount is {daily_sale_amount}")


# occupancyPercentage: calculate occupancy percentage.
    def occupancyPercentage(self):
        print(f"Occupancy rate is : {self.occupiedCnt / self.numOfRooms * 100}%")


# End of class Hotel.

# Main program.
#Build Hotel.
hotel_name = "Ocean View Hotel"
hotel_location = "Route 287 N"
my_hotel = Hotel(hotel_name, hotel_location)
print("#############################################################")
print(f"***   Welcome to {hotel_name} Administration System   ***")
print("#############################################################")

# Create rooms.
number_of_rooms = 0
NoMoreRooms = False
while number_of_rooms < 10:
    user_input = input("Do you want to create room (Yes or No)? ")
    if user_input[0].upper() == 'Y':
        room_number = int(input("Room number:"))
        bed_type = input("Type of bed (Queen, King, Twin): ")
        smoking_flag = input("Enter s for Smoking, n for Non-smoking: ")
        room_rate = float(input("Rate per night (xxx.xx): "))
        number_of_rooms += 1
        my_hotel.addRoom(room_number, bed_type, smoking_flag, room_rate)
    else:
        print("Thank you! Please visit again.")
        break


print(f"\n### {hotel_name} Administration Menu ###\n")
print("\n 1. Reservation")
print("\n 2. Cancellation")
print("\n 3. Show Reservations ")
print("\n 4. Total sales ")
print("\n 5. Rate of Occupancy")
print("\n 6. Show Rooms Details")
print("\n 0. Exit")

print("\n")

while True:
    choice = int(input("What can I help you with today?"))

    if choice == 1:
        print("Welcome to Reservation System.\n")
        rname = input("Name: ")
        bedtype = input("Type of bed: ")
        smoking = input("Room preference, enter s-Somoking, n-Non-Smoking:")
        my_hotel.addReservation(rname, smoking, bedtype)
        moreoption = input("Do you want to continue (Yes or No)? ")
        if moreoption.upper() == 'N':
            choice = 0
        else:
            continue
    if choice == 2:
        print("I am sorry, you want to cancel.")
        cname = input("Please enter occupant's name: ")
        my_hotel.cancelReservation(cname)
        moreoption = input("Do you want to continue (Yes or No)? ")
        if moreoption.upper() == 'N':
            choice = 0
        else:
            continue
    if choice == 3:
        my_hotel.printReservationList()
        moreoption = input("Do you want to continue (Yes or No)? ")
        if moreoption.upper() == 'N':
            choice = 0
        else:
            continue
    if choice == 4:
        my_hotel.getDailySales()
        moreoption = input("Do you want to continue (Yes or No)? ")
        if moreoption.upper() == 'N':
            choice = 0
        else:
            continue
    if choice == 5:
        my_hotel.occupancyPercentage()
        moreoption = input("Do you want to continue (Yes or No)? ")
        if moreoption.upper() == 'N':
            choice = 0
        else:
            continue
    if choice == 6:
        print(my_hotel.__str__())
    if choice == 0:
        break


