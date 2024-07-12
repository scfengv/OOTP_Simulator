# Issue & FAQs
2024/07/11

## Issue

### The time to create a game increases as the number of games increases

```python
def _identify_word(self):
    screenshot = ImageGrab.grab(bbox = self.region)
    self.identify_word = pytesseract.image_to_string(screenshot).strip()
    
    if self.word == self.identify_word:
        print(f"Sucessful identify {self.identify_word}")
        print("")
        self.click_success = True
        self.failures = 0

    else:
        print(f"Word: {self.word}")
        print(f"Identify word: {self.identify_word}")
        self.click_success = False

# ====== Add this line into _identify_word() in class Click =====
        if self.item != create_game:
# ===============================================================
            self.failures += 1
            if self.failures >= self.max_failures:
                self.terminate_simulator()
```

<div style="page-break-after: always;"></div>

### Fail to press enter because the delay of game UI

```python
first_attention_ok_clicker = Click(first_attention_ok)
while not first_attention_ok_clicker.click_success: 
    first_attention_ok_clicker._identify_word()
    if first_attention_ok_clicker.click_success:
        time.sleep(0.5)
        enter()
        time.sleep(0.5)

# ===== Add this while loop into all nice & ok blocks =====
        while True:
            first_attention_ok_clicker._identify_word()
            if first_attention_ok_clicker.click_success:
                print("Word still identified after pressing enter, pressing enter again.")
                enter()
                time.sleep(0.5)
                
            else:
                print("Word no longer identified after pressing enter.")
                print("")
                break # break the while True loop
        break # break the while not loop

    else:
        time.sleep(0.5)
# ========================================================
```

<div style="page-break-after: always;"></div>

### Integrate OOTP_File into OOTP_Simulator
```python
# 1. Add a Remove .lg folder func. into OOTP_File (To prevent not enough storage)
def remove_lg_folders(self):
    """
    Remove all ".lg" folders in base_dir
    """
    for item in os.listdir(self.base_dir):
        item_path = os.path.join(self.base_dir, item)
        if item.endswith('.lg') and os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"Removed folder: {item}")



# 2. Change main() of OOTP_File into other name (such as ootp_file)
def ootp_file():
    base_dir = '/path/to/saved_games'
    organized_path = '/path/to/organized_path'
    
    for item in os.listdir(base_dir):
        ...

# ===== Add remove_lg_folders() here =====
    file_operator.remove_lg_folders()
# ========================================



# 2.5 import in ootp_simulator
from ootp_file import ootp_file



# 3. Move & Remove in main() of ootp_simulator
def main():
    ...
    
# ====== Add a "start_game" parameter to help code decide when to Move & Remove folders =====
    start_game = 351

# ===== Add a while loop outside the for loop =====
    while True:
        for file_index in df.index[start_game:start_game + 1]:
            ...

            gc.collect() # Garbage Collector, it may help when loop through hundred of games
            start_game += 1

# ===== Execute ootp_file() every 100 games =====
            if start_game % 100 == 0:
                ootp_file()
                print(f"Move and Delete Game files before {start_game}")
```

<div style="page-break-after: always;"></div>

## FAQ

### The position of Next month
The position of "Next month" will be slightly different, depending on whether there is a game today. It's ok if your mouse click on "Next week" before Mar. 20th.

<img src="image-1.png" alt="drawing" height="300"/>
<img src="image.png" alt="drawing" height="300"/>