class PartyAnimal():
    x=0
    def party(self): 
        self.x = self.x +1 
        print("so far",self.x,"까지 왔다")

    
an = PartyAnimal() 

an.party()
an.party()
an.party()