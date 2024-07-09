import time
import pyautogui
import pytesseract
import pyscreenshot as ImageGrab

print("Point to the Left Top corner")
time.sleep(2)
left_x, top_y = pyautogui.position()
print("Position get")

time.sleep(1)
print("Point to the Right Bottom corner")
time.sleep(2)
right_x, bottom_y = pyautogui.position()
print("Position get")

region = (left_x, top_y, right_x, bottom_y)
screenshot = ImageGrab.grab(bbox = region)

## You can save the figure to check what have been captured
# screenshot.save("screenshot.png")

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

text = pytesseract.image_to_string(screenshot)

if text != "":
    print("Extracted Text:")
    print(text)
else:
    print("Get None")
print("")

print(f"Region: {region}")