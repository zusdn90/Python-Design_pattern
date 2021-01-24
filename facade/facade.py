# ex) 결혼 준비
# 클라이언트 - 나 / 퍼사드 - 웨딩플래너 / 서브시스템 - 음식, 호텔예약, 꽃 장식을 담당하는 업체

# 퍼사드 클래스
class EventManager(object):
    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")
    
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()
        
        self.florist = Florist()
        self.florist.setFlowerRequirements()
        
        self.caterer = Caterer()
        self.caterer.setCuisine()
        
        self.musician = Musician()
        self.musician.setMusicType()
        
# 서브시스템
class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")
        
    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True
                
    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking\n\n")

class Florist(object):
    def __init__(self):
        print("Flower Decorations for the Event? --")
    
    def setFlowerRequirements(self):
        print("Carnations, Rose and Lilies would be used for Decorations\n\n")

class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event? --")
        
    def setCuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n") 

class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage --")
    
    def setMusicType(self):
        print("Jazz and Claasical will be played\n\n")
        
# 클라이언트
class You(object):
    def __init__(self):
        print("You:: Whoa! Marraige Arrangements??!!!")
    
    def askEventManager(self):
        print("You:: Let's Contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()
        
    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")

if __name__ == "__main__":
    you = You()
    you.askEventManager()
                                                               
                           
    