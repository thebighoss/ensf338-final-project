import LiFo_ringBuffer as lifo
import numpy as np

class user_booking:
    def __init__(self,user_id,name,time,comments):
        self.id = user_id
        self.name = name
        self.time = time
        self.comments = comments
        pass

class daily_booking:
    def __init__(self):
        self.buffer = [None] * 48
        pass
    def add_booking(self,user_booking:user_booking):
        if self.buffer[(int)(np.floor(user_booking.time * 2))] != None:
            return None   
        self.buffer[(int)(np.floor(user_booking.time * 2))] = user_booking
        return (int)(np.floor(user_booking.time * 2))

    def remove_booking(self,user_booking:user_booking):
        if self.buffer[(int)(np.floor(user_booking.time * 2))] == None:
            return None   
        self.buffer[(int)(np.floor(user_booking.time * 2))] = None
        return (int)(np.floor(user_booking.time * 2))

    def get_booking_with_user_booking(self,user_booking:user_booking):
        if self.buffer[(int)(np.floor(user_booking.time * 2))] != None:
            return None   
        return self.buffer[(int)(np.floor(user_booking.time * 2))]

    def get_booking_with_time(self,time):
        if self.buffer[(int)(np.floor(time * 2))] != None:
            return None   
        return self.buffer[(int)(np.floor(time * 2))]
    def get_all_bookings(self):
        return self.buffer.copy()
    
class booking_system:
    def __init__(self,size):
        self.buffer = lifo.ring_buffer(size,daily_booking)
        pass

    def book_room(self,day,user_booking:user_booking):
        if day > self.buffer.capacity:
            print("The System Can Only Book ",self.buffer.capacity," Days In The Future")
            return None
        buffer_cell:daily_booking = self.buffer.access_at_index(day)
        buffer_cell.add_booking(user_booking)
    def print_daily_booking(self,day):
        buffer_cell:daily_booking = self.buffer.access_at_index(day)
        all_bookings = buffer_cell.get_all_bookings()
        for i in range(len(all_bookings)):
            if type(i) == user_booking:
                print("Name :",all_bookings[i].name," Time :",all_bookings[i].time)
            else:
                print("Time :",i/2, " Is Open")
                pass



test_bookingSystem = booking_system(90)
test_booking = user_booking(535,"TEST", 12.5,"Dummy Comment")
test_booking1 = user_booking(535,"TEST2", 12.5,"Dummy Comment")
test_booking2 = user_booking(535,"TEST3", 13,"Dummy Comment")
test_bookingSystem.book_room(10,test_booking)
test_bookingSystem.book_room(10,test_booking1)
test_bookingSystem.book_room(10,test_booking2)
test_bookingSystem.print_daily_booking(10)