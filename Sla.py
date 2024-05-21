import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.keyDown("win")
pyautogui.press("up")
pyautogui.keyUp("win")

pyautogui.keyDown("shift")
pyautogui.keyDown("ctrl")
pyautogui.press("n")
time.sleep(3)


pyautogui.write("https://www2.fiap.com.br/Aluno/Home")
pyautogui.press("enter")

time.sleep(3)
pyautogui.write("rm555613")
pyautogui.press("tab")
pyautogui.write("041105")
pyautogui.press("tab")
pyautogui.press("enter")
chrome
