import board
import busio
import digitalio
import adafruit_rfm9x
import time

RADIO_FREQ_MHZ = 915.0

cs = digitalio.DigitalInOut(board.GP18)
reset = digitalio.DigitalInOut(board.GP17)
spi = busio.SPI(board.GP10, MOSI=board.GP11, MISO=board.GP12)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, RADIO_FREQ_MHZ)

while True:
    try:
        packet = rfm9x.receive()
        if packet is not None:
            message = str(packet, "utf-8")
            print("Received:", message)
    except Exception as e:
        print("Error:", e)