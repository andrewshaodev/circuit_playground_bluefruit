import board, neopixel, time, digitalio
from adafruit_debouncer import Button
from audiocore import WaveFile
from audiopwmio import PWMAudioOut as AudioOut
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, \
    PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK

light_position = -1

def play_sound(filename):
    with open("drumSounds/" + filename, "rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass

def move_dot(position, direction, color):
    if color == RED:
        filename = "drum_cowbell.wav"
    else:
        filename = "scratch.wav"
    play_sound(filename)
    pixels[position] = BLACK
    position = position + direction
    position = 9 if position < 0 else position
    position = position % 10
    pixels[position] = color
    return position


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

audio = AudioOut(board.SPEAKER)

while True:
    button_A.update()
    button_B.update()
    if button_A.pressed:
        light_position = move_dot(light_position, 1, RED)
    elif button_B.pressed:
        light_position = move_dot(light_position, -1, BLUE)
