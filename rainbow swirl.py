import time

import board
import digitalio
from adafruit_circuitplayground import cp
from rainbowio import colorwheel

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.DOWN

led = cp.pixels
led.brightness = 0.1

offset = 0
BAP = False
BBP = False

blinky_time = 0.2
last_blinky = -1

while True:
    now = time.monotonic()
    if button_a.value and button_b.value:
        BAP = False
        BBP = False
    elif button_a.value:
        BAP = True
        BBP = False
        cp.red_led = False
    elif button_b.value:
        BAP = False
        BBP = True
        cp.red_led = False
    for j in range(len(led)):
        if BAP:
            led[j] = colorwheel((j * 256 // len(led) + offset) % 256)
        elif BBP:
            led[j] = colorwheel((j * 256 // len(led) - offset) % 256)
        else:
            led[j] = 0
    if not BAP and not BBP and now >= last_blinky + blinky_time:
        cp.red_led = not cp.red_led
        last_blinky = now

    led.show()
    offset = (offset + 20) % 256
    time.sleep(0.01)
