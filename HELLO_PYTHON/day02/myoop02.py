class Xi:
    def __init__(self):
        self.money = 1000
    def steal(self,smoney):
        self.money += smoney
        
 
class Putin:
    def __init__(self):
        self.nuclear = 5000
    def dementia(self):
        self.nuclear -= 1
        
        
class JungEun:
    def __init__(self):
        self.missile = 10000
    def ssorau(self):
        self.missile -= 100


class SungWoo(Xi,Putin,JungEun):
    def __init__(self):
        super().__init__()
        self.takeoff = 500
        
    def ask(self):
        self.takeoff += 1            
        
        
         
s = SungWoo()           
print(s.money)
print(s.nuclear)
print(s.missile)