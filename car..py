class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    def start(self):
        if not self.is_running:
            print(f"The {self.year} {self.make} {self.model} is now running")
            self.is_running = True
        else:
            print("car is already running")
    def stop(self):
        if self.is_running:
            print(f"the {self.year} {self.make} {self.model} has been sopped")
            self.is_running = False
        else:
            print("the car is already stopped")
            


my_car=car(make="toyota",model="camery",year=2020)
make = input('enter the company: '),
model = input("enter the model: "),
year = int(input('enter the year'))

my_car.start()
my_car.stop()