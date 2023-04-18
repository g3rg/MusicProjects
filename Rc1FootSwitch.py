import board
import digitalio
from adafruit_debouncer import Debouncer

# 2 x Foot switches, or 3? Stop, Delete, Undo
# Can a relay be used to switch audio socket as well? Would SPST work there,
# or would that leave floating ground interference yadda yadda?
#


pin = digitalio.DigitalInOut(board.D12)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP
switch = Debouncer(pin)
# switch = Debouncer(pin, interval=0.05) # default is 0.01

while True:
    switch.update()

    # if switch.value
    if switch.fell:
        print("Just pressed")
    if switch.rose:
        print("Just released")

