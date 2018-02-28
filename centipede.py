"""
Centipede for Chromebook for CircuitPython
Copyright (c) 2018, Brent Rubell for Adafruit Industries

Centipede_for_Chromebook_Enrollment by Amplified_Labs
Copyright (c) 2016, Amplified IT
See the full description at http://labs.amplifiedit.com/centipede

Support forums are available at https://plus.google.com/communities/100599537603662785064
Published under an MIT License https://opensource.org/licenses/MIT
"""

import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import board
import neopixel
import digitalio

# Modify the following to fit WiFi/Enrollment credentials:
wifi_name = "adafruit_ssid"
wifi_pass = "adafruit_password"
"""
wifi_security options:
0 = open
1 = WEP
2 = WPA
"""
wifi_security = 2
username = "circuit"
pasword = "python"

kbd = Keyboard()
# american keyboard layout
layout = KeyboardLayoutUS(kbd)

# we're going to make this button compatable with the
# builtin A button on the Circuit Playground Express
start_btn = digitalio.DigitalInOut(board.D4)
start_btn.direction = Direction.INPUT
start_button.pull = Pull.UP

# using builtin cplayx led
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

def repeat_key(key, num_repeat):
# repeats keypresses int num_repeat times
    for x in range(0, num_repeat):
        kbd.press(keycode.key)
        kbd.release_all()
        time.sleep(1)

def wifi_config():
    repeat_key(TAB, 3)
    kbd.press(keycode.ENTER)
    kbd.release_all()
    # up arrow 2 times to open extra wifi settings
    repeat_key(tab, 2)
    kbd.press(keycode.ENTER)
    kbd.release_all()
    time.sleep(1)
    # SSID Config
    #TODO: split the ssid into strings so the keyboard can write it?
    time.sleep(1)
    kbd.press(keycode.TAB)
    time.sleep(1)
    if(wifi_security == 0):
        repeatKey(TAB, 2)
    else:
        # type in wifi pass

    kbd.press(keycode.ENTER)
    time.sleep(.1)
    time.sleep(10)
    kbd.press(keycode.TAB)
    kbd.press(keyboard.ENTER)
    time.sleep(.2)
    # enter entrollment
    kbd.press(keyboard.ENTER)
    time.sleep(1)


while True:
    time.sleep(4)
    if(start_btn.value == 1):
        # run wifi config
        led.value = 1
        wifi_config()
        time.sleep(5)
        while(start_btn.value != 1):
            time.sleep(1)
        led.value = 0
        # run credential config
        credential_config()
        # pulse the neopixel ring
