class Thermometer:
    def __init__(self):
        self.displays = list()
        self.temperature = 0

    def add_display(self, display):
        if display not in self.displays:
            self.displays.append(display)

    def remove_display(self, display):
        if display in self.displays:
            self.displays.remove(display)

    def notify_displays(self):
        for display in self.displays:
            display.update()

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, new_temperature):
        if new_temperature != self.temperature:
            self.temperature = new_temperature
            self.notify_displays()
