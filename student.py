class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.model = model
        self.company = company
        self.speed_limit = speed_limit
    
    def start(self):
        print("car started")
    
    def stop(self):
        print("car stopped")
    
    def accelerate(self):
        print("car accelerating")

    def change_gear(self, gear_type):
        print("gear changed")

porche = Car("panemera", "grey", "porche", 100)
print(porche.start())
print(porche.stop())
print(porche.accelerate())

print(porche.color)