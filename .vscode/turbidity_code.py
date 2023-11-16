import board
from analogio import AnalogIn
import board
import time

analog_in = AnalogIn(board.A0)
def get_voltage(pin):
    return (pin.value * 3.3) / 65536
x = get_voltage(analog_in)
turbidity = (-1120.4*(x**2) + 5742.3*(x) - 4352.9)
while True:
    print((turbidity))
    time.sleep(10)
    

