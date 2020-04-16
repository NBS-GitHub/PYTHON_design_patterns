from observer.observables.thermometer import Thermometer
from observer.observers.display import Display

# OBSERVER PATTERN ################################################################

print("\n--- OBSERVER PATTERN\n")

# Create the observable
thermometer = Thermometer()

# Create the observers
phone_display = Display(thermometer, "Phone Display")
kitchen_display = Display(thermometer, "Kitchen Display")

# Add the observers to the observable
thermometer.add_display(phone_display)
thermometer.add_display(kitchen_display)

# Change the data
thermometer.set_temperature(12.4)
print()
thermometer.set_temperature(10.5)
print()
thermometer.set_temperature(10.5)

# Delete an observer
thermometer.remove_display(kitchen_display)

# Change the data
thermometer.set_temperature(9.7)