class Car:
    wheel = 4
    door = 2
    light = 4
    
    def __init__(self, model, year, make="Ford"):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        self.is_moving = False
        
    def using_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True
    
    def stop(self):
        if self.is_moving:
            print('The car has stopped')
            self.is_moving = False
        else:
            print('The car has already stopped')
        
    def go(self, speed):
        if self.using_gas():
            if not self.is_moving:
                print('The car starts moving')
                self.is_moving = True
            print(f'The car is going {speed}')
        else:
            print('You have run out of gas')
            self.stop()
        
    
        
        
car_one = Car('Model T', 1908)
car_one.stop()
car_one.go('slow')
car_one.go('fast')
car_one.stop()
car_one.stop()