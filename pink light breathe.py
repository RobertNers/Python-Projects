import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3)

while True:
    pixels.fill((102, 0, 51))
    time.sleep(0.2)
    pixels.fill((153, 0, 76))
    time.sleep(0.1)
    pixels.fill((204, 0, 102))
    time.sleep(0.1)
    pixels.fill((255, 0, 127))
    time.sleep(0.2)
    pixels.fill((204, 0, 102))
    time.sleep(0.1)
    pixels.fill((153, 0, 76))
    time.sleep(0.1)
    pixels.fill((102, 0, 51))
    time.sleep(0.2)
