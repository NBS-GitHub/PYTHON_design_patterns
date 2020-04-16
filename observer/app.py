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
thermometer.add_observer(phone_display)
thermometer.add_observer(kitchen_display)

# Change the data
thermometer.set_data(12.4)
print()
thermometer.set_data(10.5)
print()
thermometer.set_data(10.5)

# Delete an observer
thermometer.remove_observer(kitchen_display)

# Change the data
thermometer.set_data(9.7)