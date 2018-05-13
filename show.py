import pyautogui
import aircv as ac
import win32gui
import time
import random

def findWindowhwnd(programName='[#] 阴阳师-网易游戏 [#]'):
	return win32gui.FindWindow(None, programName)

def findWindowAndReturnRectInfo():
	hwnd = findWindowhwnd()
	left, top, right, bot = win32gui.GetWindowRect(hwnd)
	width = right - left
	height = bot - top
	return (left+10, top, width-20, height-10)

def takeImgOfTargetedProgram(saveAs,position):
	win32gui.SetForegroundWindow(findWindowhwnd())
	pyautogui.screenshot(saveAs,region=position)

def findObjectPositionInImg(imsrc, imsch):
	img = ac.imread(imsrc) 
	obj = ac.imread(imsch)
	if ac.find_template(img, obj):
		x, y = ac.find_template(img, obj)['result']
		return x, y
	else:
		return None
def theExactPoint(target):
	actualPosition = findWindowAndReturnRectInfo()
	imgPosition = findObjectPositionInImg('program.png',target)
	left, top, width, height = actualPosition
	x, y  = imgPosition
	return x + left, y + top

def takeALookAtYYS():
	takeImgOfTargetedProgram('program.png',findWindowAndReturnRectInfo())
	sleepRandom(2)

def moveTo(location):
	pyautogui.moveTo(location)
	sleepRandom(2)

def click():
	pyautogui.click()
	sleepRandom(1)

def declineInvite():
	img = ac.imread('program.png') 
	obj = ac.imread('xuanshang.PNG')
	x = ac.find_template(img, obj)
	if x:
		moveTo(theExactPoint('jujue.PNG'))
		click()

def sleepRandom(num):
	time.sleep(random.uniform(0, num))

def IsPiPeiZhong():
	takeALookAtYYS()
	img = ac.imread('program.png') 
	obj = ac.imread('pipeizhong.PNG')
	x = ac.find_template(img, obj)
	if x:
		return True
	else:
		return False

def shiju():
	time = 0
	takeALookAtYYS()
	moveTo(theExactPoint('zudui.PNG'))
	click()
	takeALookAtYYS()
	moveTo(theExactPoint('quanbu.PNG'))
	pyautogui.scroll(-1000)
	takeALookAtYYS()
	moveTo(theExactPoint('shiju.PNG'))
	click()
	takeALookAtYYS()
	moveTo(theExactPoint('zidongpipei.PNG'))
	click()
	while IsPiPeiZhong:
		time += 1
		strd = "waiting..." + str(time)
		sleepRandom(2)
		print(strd, end='')
		print('\b' * len(strd), end='', flush = True)
def upAndRunning():
	try:
		while True:
			sleepRandom(1)
			takeALookAtYYS()
			declineInvite()	

	except KeyboardInterrupt:
		print("gg")
shiju()