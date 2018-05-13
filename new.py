from pywinauto import Application
import win32gui
import win32ui
app = Application().connect(title_re="阴阳师-网易游戏")
hwnd = win32gui.FindWindow(None, '阴阳师-网易游戏')
app2 = Application().connect(handle=hwnd)
print(app,app2)