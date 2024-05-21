import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.keyDown("win")
pyautogui.press("up")
pyautogui.keyUp("win")

pyautogui.write("https://gemini.google.com/app")
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=636, y=804)

pyautogui.write("liste os nomes completos dos filhos de Harry Potter")
pyautogui.press("enter")
