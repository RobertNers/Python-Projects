# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# Modified by Robert N.

import time

from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.01

minimum_temp = 22
maximum_temp = 38


def scale_range(value):
    return int((value - minimum_temp) / (maximum_temp - minimum_temp) * 10)


def main():
    last_press = 0
    display_time = 4
    while True:
        peak = scale_range(cp.temperature)
        print(cp.temperature)
        print(int(peak))

        if peak < 0:
            cp.pixels[0] = (255, 255, 255)
        elif peak == 0:
            cp.pixels[0] = (0, 255, 255)
        elif peak > 10:
            cp.pixels[9] = (255, 0, 0)
        else:
            for i in range(10):
                if i < peak:
                    cp.pixels[i] = (0, 255, 255)
                else:
                    cp.pixels[i] = (0, 0, 0)

        if cp.button_a or cp.button_b:
            last_press = time.monotonic()
        if time.monotonic() - last_press < display_time:
            cp.pixels.show()
        else:
            cp.pixels.fill((0, 0, 0))
            cp.pixels.show()

        time.sleep(0.05)


main()
