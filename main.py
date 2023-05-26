import time
import pyautogui as pt

print("click on logged-in browser")
screenSize = pt.size()
time.sleep(3)

pt.hotkey("command", "t", interval=0.25)
# google photos images link
pt.write("https://photos.google.com/u/2/photo/AF1QipPIzz2HcgJM63yBIkc2Rk-OVYHV2UXlZcmuz4ku")
pt.hotkey('return')
time.sleep(2)

try:
    # x = pt.locateOnScreen("images/shareIcon.png", confidence=.8)
    x = pt.locateCenterOnScreen("images/shareIcon.png", confidence=.8)
    y = x[1] / 2
    xx = x[0] / 2
    pt.moveTo(xx, y, duration=1)
    pt.click()
    time.sleep(1)

    pt.write("hasibul.rupok@gmail.com")
    currentPosition = pt.position()
    x, y = currentPosition
    pt.moveTo(screenSize[0]/2, screenSize[1]/2 - 70, duration=0.5)
    pt.click()
    time.sleep(3)

    pt.write("demo file shared")
    time.sleep(1)
    # pt.hotkey('return')

except:
    print("Position not found")
