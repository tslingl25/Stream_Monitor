import board
from analogio import AnalogIn
import board
import time

offset = 0
analog_in = AnalogIn(board.A0) # Defines GP0 as the analog pin we are using
def get_voltage(pin): # Sets up a function to measure the voltage in the GPO pin
    return (pin.value * 5) / 65536
x = get_voltage(analog_in)
phValue = 3.5 * x + offset