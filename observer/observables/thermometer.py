from observer.observables.observable import Observable


class Thermometer(Observable):
    def __init__(self):
        self.displays = list()
        self.temperature = 0

    def add_observer(self, display):
        if display not in self.displays:
            self.displays.append(display)

    def remove_observer(self, display):
        if display in self.displays:
            self.displays.remove(display)

    def notify_observers(self):
        for display in self.displays:
            display.update()

    def get_data(self):
        return self.temperature

    def set_data(self, new_temperature):
        if new_temperature != self.temperature:
            self.temperature = new_temperature
            self.notify_observers()
