import win32gui
import pyautogui
import os
from pathlib import Path
def capture():
	hwnd = win32gui.FindWindow(None, '阴阳师-网易游戏')
	left, top, right, bot = win32gui.GetWindowRect(hwnd)
	w = right - left
	h = bot - top
	if(Path("test.png").is_file()):
		os.remove("test.png")
	pyautogui.screenshot('test.png',region=(left,top, w, h))
