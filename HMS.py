#Hotel Management System
class Hotel:
    sortParam='name'
    def __init__(self)->None:
        self.name=''
        self.roomAvl=0
        self.location=''
        self.rating=int
        self.pricePr=0
    def __lt__(self,other):
        getattr(self,Hotel.sortParam)<getattr(other,Hotel.sortParam)
    @classmethod
    def sortByName(cls): 
        cls.sortParam='name'
    @classmethod
    def sortByRate(cls):
        cls.sortParam='rating'
    @classmethod
    def sortByRoomAvailable(cls):
        cls.sortParam='roomAvl'
    def __repr__(self) ->str:
        return "PRHOTELS DATA:\n HotelName:{}\tRoomAvailable:{}\tLocation:{}\tRating:{}\tPricePerRoom :{}".format(self.name,self.roomAvl,self.location,self.rating,self.pricePr)
        

class User:
    def __init__(self)->None:
        self.uname=''
        self.uId=0
        self.cost=0
    def __repr__(self)->str:
        return "UserName:{}\tUserId:{}\tBookingCost:{}".format(self.uname,self.uId,self.cost)
    
    
    
def PrintHotelData(hotels):
    for h in hotels:
        print(h)

def SortHotelByName(hotels):
    print("SORT BY NAME: ")
    Hotel.sortByName()
    hotels.sort()
    PrintHotelData(hotels)
    print()
    
    
    
def SortHotelByRating(hotels):
    print("SORT BY A RATING: ")
    Hotel.sortByRate()
    hotels.sort()
    PrintHotelData(hotels)
    print()
        

def PrintHotelBycity(s,hotels):
    print("HOTELS FOR {}LOCATION ARE.".format(s))
    hotelsByloc=[h for h in hotels if h.location==s]
    
    PrintHotelData(hotelsByloc)
    print()
    
    
def SortByRoomAvailable(hotels):
    print("SORT BY ROOM AVAILABLE: ")
    Hotel.sortByRoomAvailable()
    hotels.sort()
    PrintHotelData(hotels)
    print()

def PrintUserData(userName,userId,bookingCost,hotels):
    users=[]
    
    for i in range (3):
        u=User()
        u.uname=userName[i]
        u.uId=userId[i]
        u.cost=bookingCost[i]
        users.append(u)
    for i in range (len(users)):
        print(users[i],"\tHotel name: ",hotels[i].name)


def HotelManagement(userName,userId,hotelName,bookingCost,rooms,locations,ratings,prices):
    
    hotels=[]
    
    for i in range(3):
        h=Hotel()
        h.name=hotelName[i]
        h.roomAvl=rooms[i]
        h.location=locations[i]
        h.rating=ratings[i]
        h.pricePr=prices[i]
        hotels.append(h)
    print()
    
    PrintHotelData(hotels)
    SortHotelByName(hotels)
    SortHotelByRating(hotels)
    PrintHotelBycity("Bangalore",hotels)
    SortByRoomAvailable(hotels)
    PrintUserData(userName,userId,bookingCost,hotels)
if __name__=='__main__':
        userName=['basma','nasma','hamsa']
        userId=[2,4,3]
        hotelName=['H1','H2','H3']
        bookingCost=[1000,1200,1233]
        rooms=[2,4,5]
        locations=["Bangalore",'mine','cairo']
        ratings=[3,6,5]
        prices=[100,233,544]
        
        
HotelManagement(userName,userId,hotelName,bookingCost,rooms,locations,ratings,prices)