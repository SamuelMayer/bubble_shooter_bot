import pyautogui
import time

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        position_str = f'\033[2K\rX: {x} Y: {y}'
        print(position_str, end='', flush=True)
        time.sleep(0.1)

except KeyboardInterrupt:
    print('\nProgramm beendet.')
