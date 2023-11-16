import board
from analogio import AnalogIn
import board
import time

analog_in = AnalogIn(board.A0) # Defines GP0 as the analog pin we are using
def get_voltage(pin): # Sets up a function to measure the voltage in the GPO pin
    return (pin.value * 3.3) / 65536 # equation to measure the voltage value
x = get_voltage(analog_in) # Defines x as the variable used in the turbidity equation to represent the voltage
turbidity = (-1120.4*(x**2) + 5742.3*(x) - 4352.9) # turbidity equation where y is turbidity and x is voltage, allows turbidity to be graphed
while True:
    print((turbidity)) # prints the turbidity value
    time.sleep(10)
    

