# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

num = 11

# The number of NeoPixels
num_pixels = 12

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGBW

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=.1, auto_write=False, pixel_order=ORDER
)

#while True:
pixels.fill((255, 255, 255, 0))
#    pixels.fill((0, 0 ,0 , 0))
#    pixels[num] = (255, 255, 255, 0)
pixels.show()
time.sleep(40)
pixels.fill((0, 0 ,0 , 0))
pixels.show()

quit()

