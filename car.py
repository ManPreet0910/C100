class Car(object):
    def __init__(self, model, color, company):
        self.model = model
        self.color = color
        self.company = company
    
    def start(self):
        print("Started")

    def stop(self):
        print("stopped")

car1 = Car("xyz", "green", "Honda" )
car1.start()
