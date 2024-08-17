import board, neopixel, time, digitalio
from adafruit_debouncer import Button
from audiocore import WaveFile
from audiopwmio import PWMAudioOut as AudioOut
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, \
    PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

colors = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD,
    PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK]

button_A_input = digitalio.DigitalInOut(board.BUTTON_A)
button_A_input.switch_to_input(digitalio.Pull.DOWN)
button_A = Button(button_A_input, value_when_pressed = True)

button_B_input = digitalio.DigitalInOut(board.BUTTON_B)
button_B_input.switch_to_input(digitalio.Pull.DOWN)
button_B = Button(button_B_input, value_when_pressed = True)

speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True

while True:
    button_A.update()
    button_B.update()
    if button_A.pressed:
        pixels.fill(BLUE)
    elif button_A.released:
        pixels.fill(BLACK)
    elif button_B.pressed:
        pixels.fill(RED)
    elif button_B.released:
        pixels.fill(BLACK)
