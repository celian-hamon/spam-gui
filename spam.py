import pyautogui, time, pyperclip

def spamfct(text,reps,speed):
    pyperclip.copy(text)
    for i in range(reps):
        time.sleep(float(speed*0.1))
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")