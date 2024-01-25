import time
import board
import analogio

ph_sensor_pin = board.A0

analog_ph = analogio.AnalogIn(ph_sensor_pin)

def read_ph_voltage():
    raw_value = analog_ph.value
    voltage = raw_value / 65535 * 3.3 

    return voltage

def convert_voltage_to_ph(voltage):
    ph_value = 3.5 * voltage - 1.5

    return ph_value

while True:
    ph_voltage = read_ph_voltage()
    ph_value = convert_voltage_to_ph(ph_voltage)
    print("pH Value:", ph_value)
    time.sleep(1)
