import time
import board
import adafruit_onewire
import adafruit_ds18x20

# Define the OneWire bus using pin GP17
onewire_bus = adafruit_onewire.OneWire(board.GP17)

# Create a DS18X20 sensor object
ds18b20 = adafruit_ds18x20.DS18X20(onewire_bus)

# Scan for DS18X20 devices on the bus
devices = ds18b20.scan()

if not devices:
    raise RuntimeError("No DS18B20 devices found.")

while True:
    # Get temperature from all DS18B20 devices
    temperatures = [ds18b20.temperature for ds18b20 in devices]

    # Print temperature for each device
    for i, temperature in enumerate(temperatures):
        print(f"Temperature Sensor {i + 1}: {temperature:.2f}°C")

    # Wait for some time before taking the next reading
    time.sleep(1)
