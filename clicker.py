import keyboard,mouse,time

isClicking = False

def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("clocker off")
    else:
        isClicking = True
        print("clocker on")

keyboard.add_hotkey('esc',set_clicker)

while True:
    if isClicking:
        mouse.click(button = 'left')
        time.sleep(0.01)