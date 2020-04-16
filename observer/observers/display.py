from observer.observers.observer import Observer


class Display(Observer):
    def __init__(self, thermometer, display_name):
        self.thermometer = thermometer
        self.display_name = display_name
        self.temperature = 0

    def update(self):
        self.temperature = self.thermometer.get_temperature()
        self.display()

    def display(self):
        print(self.display_name, ": The current temperature is", str(self.temperature) + ". ")
