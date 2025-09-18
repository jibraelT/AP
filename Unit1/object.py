# object is  a construct for story data and function.
# when creating an object we start  with the classs keypad
# This acts like our object maker/ our blueprint
class CarMaker:
    def __init__(self, name, color, seating, year, model, miles): # Initialize blueptint
        self.name = name 
        self.color = color
        self.seating = seating
        self.year = year
        self.model = model
        self.miles = miles
    
    def printInfo(self):
        print('heres yor car faqs')
        print('name:'+self.name)
        print('year:'+ str(self.year))
        print('miles'+ str(self.miles))


    def windshieldwippers():
        print("when raining turn on ")
    def airnag():
        print("when going into a collission pop out")
    def turnsignals(up,down):
        if up:
            print("turn left")
        elif down:
            print("turn right ")
    
    def bluetooth(year):
        if year > 2020:
            print("you have bluetooth")

carOption1 = CarMaker('carolla','black','','2024','coralla','miles')

print(carOption1)

carOption1.printInfo()





class Phone:
    def _init_(self,name,color,cameras,number):
        self.name = name 
        self.color = color
        self.cameras = cameras
        self.number = number
    
    def printInfo(self):
        print('here are your phone faqs')
        print('name:'+ self.name)
        print('color:'+ str(self.color))
        print('cameras:'+ str(self.cameras))
        print('number:'+ str(self.number))
    
    def number(rung, ):
        if rung:
            print("ring ,ring, ring")

        if rung > 3:
            print("hang up")

phoneA =  Phone('Iphone15','black','4','24')
            






















































































