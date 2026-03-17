import FiFo_ringBuffer as fifo
import LiFo_ringBuffer as lifo
import room_booking as rb
import traversal as tv
import random as rd
path_way_graph = tv.graph()


class Campus:
    def __init__(self):
        self.buildings = {} # building_id -> Building
        self.pathways = ... # your chosen network representationV

class Room: #Provided By Assignemnt
    def __init__(self, capacity: int, room_type: str,split_room :list = None):
        self.capacity = capacity # max occupancy
        self.room_type = room_type # "lecture", "lab", "office"
        self.bookings = rb.booking_system(30) # list of Booking objects
        self.split_room = split_room
class Floor:
    def __init__(self):
        self.rooms = []

class Building: #Provided By Asssignment
    def __init__(self, building_id : int,building_name: str, name: str, location: tuple):
        self.building_id = building_id # e.g. unique ID
        self.building_name = building_name.lower() #e.g. "ICT"
        self.name = name # "Information and Comm. Tech."
        self.location = location # (lat, lon) or grid coords
        self.floors = [] # room_id -> Room

def find_room(floor : Floor,room_number) -> Room:
    return floor.rooms[room_number]
def find_floor(building:Building,floor_number) -> Floor:
    return building.floors[floor_number]
def find_building(campus:Campus,building_name:str= None,building_id:int = None) -> Building:
    if building_id != None:
        return campus.buildings.values(building_id)
    elif building_name != None:
        return campus.buildings[building_name]

def room_finder(floor_number:int , room_number :int,campus:Campus,building_name:str= None,building_id:int = None) -> list:
    building = find_building(campus=campus,building_name="ENG",building_id=None)
    floor = find_floor(building,floor_number=floor_number)
    room = find_room(floor,room_number=room_number)
    print(room)
    return [building,floor,room]


####
room_types = ["Study","Confrense","Meeting","Lecture"]
###################### Constructors TFDL

building_list = {}
building_name_list = ["TFDL","ENG","ICT","SCA","SCB","SCT","MUFR","ADM","HSKYN","MAC"]
building_count = 10

floor_list = [] 
floor_count = 15
room_count = 40
for k in range(building_count):
    building_list[building_name_list[k]] = (Building(k,building_name_list[k],building_name_list[k],[0,0]))
    for j in range(floor_count):
        building_list[building_name_list[k]].floors.append(Floor())
        floor_list.append(Floor())
        for i in range(room_count):
            building_list[building_name_list[k]].floors[j].rooms.append(Room(rd.randint(0,30),room_types[rd.randint(0,len(room_types)-1)]))
for i in (building_list):
    print(i)
campus = Campus()
campus.buildings = dict(building_list)

return_val = room_finder(4,23,campus=campus,building_name="ENG")
test_bookingSystem = return_val[2].bookings
print(return_val[0].name)

print(return_val[1])
print(return_val[2].bookings)

test_booking = rb.user_booking(535,"TEST", 12.5,"Dummy Comment")
test_booking1 = rb.user_booking(535,"TEST2", 12.5,"Dummy Comment")
test_booking2 = rb.user_booking(535,"TEST3", 13,"Dummy Comment")
return_val[2].bookings.book_room(3,test_booking)
return_val[2].bookings.book_room(4,test_booking1)
return_val[2].bookings.book_room(5,test_booking2)
return_val[2].bookings.print_daily_booking(3,0,15)
return_val[2].bookings.print_daily_booking(4,0,15)
return_val[2].bookings.print_daily_booking(5,0,15)