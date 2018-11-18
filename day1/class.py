
class PartyAnimal(): 

    z=0

    def __init__(self,x,y):
        self.name = x 
        self.age = y 
        print(self.name,self.age,"나는 생성자입니다.")


    def start(self): 
        self.z = self.z + 1
        print("so far",self.z)


ab = PartyAnimal("Han sang woo",29)
ac = PartyAnimal("kim sang in",39)


class FootballFan(PartyAnimal): 
    points =0 
    
    def touchdown(self): 
        self.points = self.points + 7 
        self.start() 
        print(self.name,"points",self.points)


s= PartyAnimal("han",20)
s.start() 


j=FootballFan('sang',21)
j.start() 
j.touchdown()


# 상속의 개념 공부   기본적인 클래스와 