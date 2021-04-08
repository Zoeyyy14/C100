class Car(object):
    def __init__(self, model, company, color, speed_limit):
        self.model = model
        self.company = company
        self.color = color
        self.speed_limit = speed_limit

    def start(self):
        print("Car Has Started")
    
    def stop(self):
        print("Car Has Stoped")

    def accelerate(self):
        print("Car Has Accelerated")

    def speed(self):
        print("I Have a High Speed Car")

Tesla = Car("A7", "Tesla", "purple", 100)
print(Tesla.start())
print(Tesla.stop())
print(Tesla.accelerate())
print(Tesla.speed())