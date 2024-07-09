import pytesseract
import pyscreenshot as ImageGrab

# (left_x, top_y, right_x, bottom_y)
region = (150, 515, 265, 540)

screenshot = ImageGrab.grab(bbox = region)

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

text = pytesseract.image_to_string(screenshot)

print("Extracted Text:")
print(text)