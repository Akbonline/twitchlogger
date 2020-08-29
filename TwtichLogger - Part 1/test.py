import keyboard
import time
def something():
    print("This workS!!!")
    quit()


if __name__ == "__main__":
    keyboard.add_hotkey( "esc", something)
    time.sleep(5)