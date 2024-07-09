# OOTP Update
2024/07/09


## Update since 2024/07/04

With the assist of Optical Character Recognition to verify that each step is performed correctly
- `pip install -r requirements.txt`
  
  Ignore the error if there is a problem installing `pytesseract`

## Click
- Install `pytesseract` package (by homebrew)
  - Windows OS can ask 鄭竹淇
  - Mac (in cmd):
    - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    - `brew install tesseract`
  
- Update `pytesseract.pytesseract.tesseract_cmd` @ `utils.py` line 151
  - Mac: use `which tesseract` in cmd (Apple silicon: `"/opt/homebrew/bin/tesseract"`)
- `auto_click`: click and verify
- `normal_click`: only click, use it when nothing really change (need `sleep`)
- `while not ... enter()`: ref. `create_game`, `nice` & `ok` in `utils.py`. A little logic is required here (the opposite logic from `auto_click`), but it shouldn't be too hard

```python
class Click:
  """
  3 Instance attributes (item.position, item.region, item.word)
  2 Instance method
  1 Terminate
  """
  def _auto_click(self):
    """
    same as before, but you might need to change the setting to that fit your computer the most
    """
    ...

  def _identify_word(self):
    """
    Use pytesseract to identify the word in item.region
    if self.word == self.identify_word:
      pass
    else:
      click again
    """
    ...

  def terminate_simulator(self):
    """
    if identify fail more than max_failures (Default 10, tunable), terminate code automatically
    """
    ...
```

## Module
Represent each item to click, contain position, region, and word 

```python
class module:
    def __init__(self, position, region, word) -> None:
        self.position = position
        self.region = region
        self.word = word
```

`module.position`: stands for where to click (same as before)

![alt text](<md/截圖 2024-07-09 16.45.47.png>)

`module.region`: 
- stands for the region to verify whether `click` has properly executed. It should contain **words** **that only appear after `click`**
- `(left_x, top_y, right_x, bottom_y)`: the x&y of that two yellow points in Example 1
- It is **safer** to get the region as **big** as possible, as long as not containing other irrelevant words

`module.word`: stands for the **words** inside the region

```python
# Example 1
FirstGame_new_game = module(
    position = (181, 532),
    region = (147, 757, 416, 784), ## Get NEW QUICKSTART GAME -> which means FirstGame_new_game had successfully click
    word = "NEW QUICKSTART GAME"
)
```

![alt text](<md/截圖 2024-07-09 16.45.57.png>)

```python
# Example 2
play_button = module(
    position = (901, 85),
    region = (834, 142, 919, 160),  ## Get "Finish Today!" after "Play" was clicked
    word = "Finish Today!"
)
```
![alt text](<md/截圖 2024-07-09 20.35.29.png>)

### Get region

- You can use `get_position_region.py` to get the region
```python
    # get_position_region.py

    1. Point at the Top Left corner 
    -> Position get

    2. Move to the Right Bottom corner
    -> Position get

    return region (tuple of 4)
```

- You can use `test_region.py` to check what will the computer get in that region


## Change batter sequence
The place to change batter sequence has changed.

![alt text](<md/截圖 2024-07-09 17.10.27.png>)


## Notice

### 1
If you are not familiar with the process, you can print everything out in cmd. Please ref. `終端機輸出記錄.txt`

```python
## Sucess at the first try
Sucessful identify NEW QUICKSTART GAME
```

```python
Word: Attention!
Identify word:  ## Fail to identify words at the first try (Game is still loading) -> click again
Sucessful identify Attention!  ## Sucess at the second try
```

### 2
I removed almost all `sleep` because OCR perform solid on my computer, but feel free to add it back.